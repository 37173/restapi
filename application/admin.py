from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Dessert)
admin.site.register(Client)
admin.site.register(Pay)
admin.site.register(Order)
admin.site.register(OrderDetail)