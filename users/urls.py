from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('login/', views.login_view, name='users-login'),
    path('logout/', views.logout_view, name='users-logout'),
    # path('information/', login_required(views.FormWizardView.as_view(views.INFORMATION_WIZARD_FORMS)), name='users-information'),
    path('done/', views.done, name='users-done'),
    path('form/', views.form_wizard, name='users-information'),
    path('form/save', views.save_form, name='users-information-save'),
]