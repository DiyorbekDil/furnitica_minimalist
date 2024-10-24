from django.contrib import admin

from ordering.models import OrderModel, OrderItemModel

admin.site.register(OrderModel)
admin.site.register(OrderItemModel)
