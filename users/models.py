from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils import timezone


# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, national_code):
        print('user manager model', national_code)
        if not national_code:
            raise ValueError('Users must have an national code')

        user = self.model(
            national_code=national_code,
        )

        password = '123456789'
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, national_code):
        user = self.create_user(
            national_code
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, national_code):
        user = self.create_user(
            national_code
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    national_code = models.CharField(
        verbose_name='national code',
        max_length=11,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.national_code

    def get_short_name(self):
        return self.national_code

    def __str__(self):
        return self.national_code

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active






class Information(models.Model):
    phone_regex = RegexValidator(regex=r'^\0?1?\d{10,11}$',
                                 message="Phone number must be entered in the format: '0999999999'")

    student_regex = RegexValidator(regex=r'\d{9}$', message="studentcode must be 9 number")

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    EDUCATION_CHOICES = [(1, 'زیر دیپلم'), (2, 'دیپلم'), (3, 'بالاتراز دیپلم')]
    LANGUAGE_CHOICES = [(1, 'کم'), (2, 'متوسط'), (3, 'زیاد')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=20)
    birthPlace = models.CharField(max_length=15, blank=True)
    birthDate = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=25)
    province = models.CharField(max_length=18)
    city = models.CharField(max_length=15)
    address = models.CharField(max_length=40)

    education = models.IntegerField(max_length=1, choices=EDUCATION_CHOICES)
    field = models.CharField(max_length=20, blank=True)
    university = models.CharField(max_length=20, blank=True)
    studentNumber = models.CharField(validators=[student_regex], blank=True)
    religousEducation = models.CharField(max_length=20)
    englishLanguage = models.IntegerField(max_length=1, choices=LANGUAGE_CHOICES, blank=True)
    arabicLanguage = models.IntegerField(max_length=1, choices=LANGUAGE_CHOICES, blank=True)

    fisically = models.IntegerField(max_length=1, choices=[(0, 'معلول'), (1, 'سالم')])
    defective = models.CharField(max_length=40, blank=True)
    disease = models.CharField(max_length=15, blank=True)
    drugs = models.CharField(max_length=15, blank=True)
#
