from django.contrib.auth import login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required, user_passes_test
import random


from .backends import PasswordlessAuthBackend
from .forms import MainForm, FormStepOne, FormStepTwo, FormStepThree
from .models import Information


def login_view(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        print('request post')
        if form.is_valid():
            national_code = form.cleaned_data.get("national_code")
            user = PasswordlessAuthBackend().authenticate(national_code=national_code)
            if user is not None:
                login(request, user)
                return redirect('users-information')
        else:
            messages.error(request, f"your national code must be include just 10 numbers")
            form = MainForm()
            return render(request, 'users/login.html', {'form': form})
    else:
        form = MainForm
        return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('blog-home')


INFORMATION_WIZARD_FORMS = (
    ("FormStepOne", FormStepOne),
    ("FormStepTwo", FormStepTwo),
    ("FormStepThree", FormStepThree)
)


class FormWizardView(UserPassesTestMixin, SessionWizardView):
    template_name = "users/wizardform.html"
    instance = None
    redirect_field_name = 'users/done.html'
    initial = {}

    def test_func(self):
        print('test_func')
        user = self.request.user
        if not user.is_complete:
            return True
        return False

    def handle_no_permission(self):
        return redirect("users-done")

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Information(user=self.request.user)
        return self.instance

    def done(self, form_list, **kwargs):
        FormStepOne, FormStepTwo, FormStepThree = form_list
        project = self.instance
        user = self.request.user
        user.setcomplete(True)
        user.save()
        project.save()
        user_information = Information.objects.get(user=user)
        rand = random.random()
        rand *= 100000
        rand = round(rand)
        return render(self.request, 'users/done.html', {
            'data': user_information,
            'random': rand
        })

    def get_form_initial(self, step):
        initial = self.initial
        try:
            userinformation = Information.objects.get(user=self.request.user)
            initial.update(userinformation.__dict__)
            return self.initial_dict.get(step, initial)
        except ObjectDoesNotExist:
            return self.initial_dict.get(step, {})

    def post(self, *args, **kwargs):
        print('def post')
        step = self.steps.current
        print(step)
        form = self.get_form(data=self.request.POST, files=self.request.FILES)

        if form.is_valid():
            if step == 'FormStepOne':
                project = self.instance
                project.save()
            elif step == 'FormStepTwo':
                userinformation = Information.objects.filter(user=self.request.user)
                education = form.cleaned_data['education']
                field = form.cleaned_data['field']
                university = form.cleaned_data['university']
                studentNumber = form.cleaned_data['studentNumber']
                religousEducation = form.cleaned_data['religousEducation']
                englishLanguage = form.cleaned_data['englishLanguage']
                arabicLanguage = form.cleaned_data['arabicLanguage']

                userinformation.update(education=education)
                userinformation.update(field=field)
                userinformation.update(university=university)
                userinformation.update(studentNumber=studentNumber)
                userinformation.update(religousEducation=religousEducation)
                userinformation.update(englishLanguage=englishLanguage)
                userinformation.update(arabicLanguage=arabicLanguage)

        return super(FormWizardView, self).post(*args, **kwargs)


def done(request):
    user_information = Information.objects.get(user=request.user)
    return render(request, 'users/done.html', {'data': user_information})
