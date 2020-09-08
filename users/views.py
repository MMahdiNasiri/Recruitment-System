from django.contrib.auth import login, logout
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


def usercomplete(user):
    return user.is_complete == False


user_login_required = user_passes_test(usercomplete, login_url='users-done')


def complete_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func


def done(request):
    user = request.user
    if user.is_authenticated and user.is_complete:
        completedata = Information.objects.get(user=user)
        return render(request, 'users/done.html', {'data':completedata})
    else:
        return redirect('users-information')



class FormWizardView(SessionWizardView):
    template_name = "users/wizardform.html"
    instance = None

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

        return render(self.request, 'users/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    @method_decorator(complete_user_required)
    def get(self, request, *args, **kwargs):
        try:
            my_form = self.get_form()
            return self.render(my_form)
        except KeyError:
            return super().get(request, *args, **kwargs)





