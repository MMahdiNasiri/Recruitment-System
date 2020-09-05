from django import forms
from django.core.validators import RegexValidator

from .models import User


class FormStepOne(forms.Form):
    national_regex = RegexValidator(regex=r'\d{10}$', message="nationalcode must be number")
    national_code = forms.CharField(validators=[national_regex])

    #
# class FormStepOne(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     phone = forms. CharField(max_length=100)
#     email = forms.EmailField()
#
# class FormStepTwo(forms.Form):
#     job = forms.CharField(max_length=100)
#     salary = forms.CharField(max_length=100)
#     job_description = forms.CharField(widget=forms.Textarea)
