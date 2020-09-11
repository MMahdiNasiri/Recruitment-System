from django.contrib.auth import login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required, user_passes_test

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

    def test_func(self):
        print('test_func')
        user = self.request.user
        if not user.is_complete:
            return True
        return False

    def handle_no_permission(self):
        return redirect("users-done")

    def get_form_instance(self, step):
        print('instance')
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

        return render(self.request, 'blog/home.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get_form_initial(self, step):
        print('get_form_initial')
        initial = {}
        userinformation = Information.objects.get(user=self.request.user)
        initial.update(userinformation.__dict__)
        return self.initial_dict.get(step, initial)


    def process_step(self, form):
        project = self.instance
        project.save()
        return self.get_form_step_data(form)



def done(request):
    return render(request, 'users/done.html', {})
