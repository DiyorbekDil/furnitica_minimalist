from django.shortcuts import render
from django.views.generic import TemplateView


class UserRegisterView(TemplateView):
    template_name = 'user-register.html'


class UserLoginView(TemplateView):
    template_name = 'user-login.html'


class UserAccountView(TemplateView):
    template_name = 'user-acount.html'


class UserResetView(TemplateView):
    template_name = 'user-reset-password.html'


class UserWishlistView(TemplateView):
    template_name = 'user-wishlist.html'



