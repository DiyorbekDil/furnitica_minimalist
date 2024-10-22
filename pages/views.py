from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from pages.forms import ContactModelForm


# class ContactView(TemplateView):
#     template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'pages/about-us.html'


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('common:home')


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class View404(TemplateView):
    template_name = 'pages/404.html'
