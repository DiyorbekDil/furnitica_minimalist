from django.shortcuts import render
from django.views.generic import TemplateView


class ProductCheckoutView(TemplateView):
    template_name = 'ordering/checkout.html'


class ProductCartView(TemplateView):
    template_name = 'ordering/cart.html'


class UserWishlistView(TemplateView):
    template_name = 'ordering/user-wishlist.html'
