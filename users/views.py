from django.shortcuts import render
from django.views.generic import TemplateView


class UserRegisterView(TemplateView):
    template_name = 'registration/user-register.html'


class UserLoginView(TemplateView):
    template_name = 'registration/user-login.html'


class UserAccountView(TemplateView):
    template_name = 'registration/user-acount.html'


class UserResetView(TemplateView):
    template_name = 'registration/user-reset-password.html'
