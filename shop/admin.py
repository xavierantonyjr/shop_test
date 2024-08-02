# shop/admin.py

from django.contrib import admin
from .models import Product, Request, UserProfile

admin.site.register(Product)
admin.site.register(Request)
admin.site.register(UserProfile)
