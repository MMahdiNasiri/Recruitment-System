from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from formtools.wizard.views import SessionWizardView

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
        project.save()

        return render(self.request, 'users/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get(self, request, *args, **kwargs):
        try:
            my_form = self.get_form()
            for myfield in my_form:
                my_form.fields[myfield].widget.attrs['readonly'] = True

            for field in my_form:
                print(field)

            return self.render(my_form)
        except KeyError:
            return super().get(request, *args, **kwargs)



