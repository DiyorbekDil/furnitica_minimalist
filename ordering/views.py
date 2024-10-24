from urllib import request

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from ordering.forms import OrderModelForm
from ordering.models import OrderItemModel
from products.models import ProductModel


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart

    return redirect(request.GET.get('next', reverse_lazy('products:product_list')))


class UserCartView(ListView):
    template_name = 'ordering/cart.html'
    context_object_name = 'products'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.objects.filter(pk__in=cart)


class OrderCreateView(CreateView):
    form_class = OrderModelForm
    template_name = 'ordering/checkout.html'
    success_url = '/'

    @staticmethod
    def add_item(order, product):
        OrderItemModel.objects.create(order=order, product=product)

    def form_valid(self, form):
        # order = form.save()
        cart = self.request.session.get('cart', [])
        if cart:
            products = ProductModel.objects.filter(pk__in=cart)
            for product in products:
                self.add_item(cart, product)
            return redirect(self.success_url)
        else:
            return redirect('products:product_list')


class UserWishlistView(TemplateView):
    template_name = 'ordering/user-wishlist.html'
