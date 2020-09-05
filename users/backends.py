from django.contrib.auth.backends import ModelBackend
from .models import User


class PasswordlessAuthBackend(ModelBackend):

    def authenticate(self, national_code):
        try:
            print('try backends authenticate', national_code)
            return User.objects.get(national_code=national_code)
        except User.DoesNotExist:
            print('exept backends autheticate', national_code)
            return User.objects.create_user(national_code=national_code)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None