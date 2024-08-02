# myproject/urls.py

from django.contrib import admin
from django.urls import path
from shop import views as shop_views

urlpatterns = [
    path('', shop_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', shop_views.register, name='register'),
    path('login/', shop_views.login_view, name='login'),
    path('logout/', shop_views.logout_view, name='logout'),
    path('products/', shop_views.list_products, name='list_products'),
    path('product/add/', shop_views.add_product, name='add_product'),
    path('product/<int:id>/', shop_views.product_detail, name='product_detail'),
    path('product/<int:id>/edit/', shop_views.edit_product, name='edit_product'),
    path('product/<int:id>/delete/', shop_views.delete_product, name='delete_product'),
    path('purchase_request/', shop_views.purchase_request, name='purchase_request'),
    path('my_requests/', shop_views.list_my_requests, name='list_my_requests'),
    path('requests/', shop_views.list_requests, name='list_requests'),
    path('request/<int:id>/approve/', shop_views.approve_request, name='approve_request'),
    path('request/send/', shop_views.send_request, name='send_request'),
]
