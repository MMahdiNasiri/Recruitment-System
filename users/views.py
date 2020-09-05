from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .backends import PasswordlessAuthBackend
# Create your views here.
from .forms import FormStepOne



def login_view(request):
    if request.method == 'POST':
        form = FormStepOne(request.POST)
        print('request post')
        if form.is_valid():
            national_code = form.cleaned_data.get("national_code")
            user = PasswordlessAuthBackend().authenticate(national_code=national_code)
            if user is not None:
                login(request, user)
                return redirect('blog-home')
        else:
            messages.error(request, f"your national code must be include just 10 numbers")
            form = FormStepOne()
            return render(request, 'users/login.html', {'form': form})
    else:
        form = FormStepOne
        return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('blog-home')


