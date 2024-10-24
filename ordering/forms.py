from django import forms

from ordering.models import OrderModel


class OrderModelForm(forms.Form):
    class Meta:
        model = OrderModel
        fields = ['full_name', 'phone_number', 'email']