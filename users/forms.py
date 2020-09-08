from django import forms
from django.core.validators import RegexValidator

from .models import User, Information


class MainForm(forms.Form):
    national_regex = RegexValidator(regex=r'\d{10}$', message="nationalcode must be number")
    national_code = forms.CharField(validators=[national_regex])


class FormStepOne(forms.ModelForm):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    phone_regex = RegexValidator(regex=r'^\0?1?\d{10,11}$',
                                 message="Phone number must be entered in the format: '0999999999'")

    firstName = forms.CharField(max_length=15)
    lastName = forms.CharField(max_length=20)
    birthPlace = forms.CharField(max_length=15, required=False)
    # birthDate = forms.DateField()
    gender = forms.TypedChoiceField(choices=GENDER_CHOICES)
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, required=False)
    email = forms.EmailField(max_length=25, required=False)
    province = forms.CharField(max_length=18, required=False)
    city = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=40, required=False)

    class Meta:
        model = Information
        fields = ['firstName', 'lastName', 'birthPlace', 'gender', 'phone_number',
                  'email', 'province', 'city', 'address']


class FormStepTwo(forms.ModelForm):
    student_regex = RegexValidator(regex=r'\d{9}$', message="studentcode must be 9 number")
    EDUCATION_CHOICES = [(1, 'زیر دیپلم'), (2, 'دیپلم'), (3, 'بالاتراز دیپلم')]
    LANGUAGE_CHOICES = [(1, 'کم'), (2, 'متوسط'), (3, 'زیاد')]

    education = forms.TypedChoiceField(choices=EDUCATION_CHOICES)
    field = forms.CharField(max_length=20, required=False)
    university = forms.CharField(max_length=20, required=False)
    studentNumber = forms.CharField(validators=[student_regex], required=False)
    religousEducation = forms.CharField(max_length=20)
    englishLanguage = forms.TypedChoiceField(choices=LANGUAGE_CHOICES, required=False)
    arabicLanguage = forms.TypedChoiceField(choices=LANGUAGE_CHOICES, required=False)

    class Meta:
        model = Information
        fields = ['education', 'field', 'university', 'studentNumber', 'religousEducation',
                  'englishLanguage', 'arabicLanguage']


class FormStepThree(forms.ModelForm):
    fisically = forms.TypedChoiceField(choices=[(0, 'معلول'), (1, 'سالم')])
    defective = forms.CharField(max_length=40, required=False)
    disease = forms.CharField(max_length=15, required=False)
    drugs = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Information
        fields = ['fisically', 'defective', 'disease', 'drugs']

