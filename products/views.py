from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import *


class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'


class CategoryListView(ListView):
    template_name = 'products/categories-filter.html'
    model = CategoryModel
    context_object_name = 'categories'


class BrandsListView(ListView):
    template_name = 'products/products-filter.html'
    model = BrandModel
    context_object_name = 'brands'


class ColorsListView(ListView):
    template_name = 'products/products-filter.html'
    model = ColorModel
    context_object_name = 'colors'


class TagsListView(ListView):
    template_name = 'products/products-filter.html'
    model = TagModel
    context_object_name = 'tags'
