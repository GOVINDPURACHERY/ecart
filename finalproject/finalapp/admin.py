from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(registration)
admin.site.register(shopreg)
admin.site.register(commonlogin)
admin.site.register(products)
admin.site.register(cart)