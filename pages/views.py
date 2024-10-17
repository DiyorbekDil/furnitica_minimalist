from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from pages.forms import ContactModelForm


# class ContactView(TemplateView):
#     template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about-us.html'


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('common:home')
