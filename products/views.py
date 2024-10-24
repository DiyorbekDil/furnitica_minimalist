from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import *


class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    def get_queryset(self):
        return ProductModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        return context
