from django.contrib import admin
from .models import Product, PurchaseRequest, Customer

admin.site.register(Product)
admin.site.register(PurchaseRequest)
admin.site.register(Customer)
