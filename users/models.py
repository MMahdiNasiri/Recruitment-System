from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, national_code, password=None):
        print('user manager model', national_code)
        if not national_code:
            raise ValueError('Users must have an national code')

        user = self.model(
            national_code=national_code,
        )
        if password is None:
            password = '123456789'
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, national_code, password):
        user = self.create_user(
            national_code,
            password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, national_code, password):
        user = self.create_user(
            national_code,
            password
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
    perm = models.BooleanField(default=True)

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
        return self.perm

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=20)
    birthPlace = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField(max_length=25)
    province = models.CharField(max_length=18)
    city = models.CharField(max_length=15)
    address = models.CharField(max_length=40)

    education = models.CharField(max_length=1)
    field = models.CharField(max_length=20, blank=True)
    university = models.CharField(max_length=20, blank=True)
    studentNumber = models.CharField(max_length=1)
    religousEducation = models.CharField(max_length=20)
    englishLanguage = models.IntegerField(default=0)
    arabicLanguage = models.IntegerField(default=0)

    fisically = models.IntegerField(default=0)
    defective = models.CharField(max_length=40, blank=True)
    disease = models.CharField(max_length=15, blank=True)
    drugs = models.CharField(max_length=15, blank=True)

