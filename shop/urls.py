from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('purchase_request/', views.purchase_request, name='purchase_request'),
    path('my_requests/', views.my_requests, name='my_requests'),
]
