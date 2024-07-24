from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', shop_views.register, name='register'),
    path('login/', shop_views.login, name='login'),
    path('logout/', shop_views.logout, name='logout'),
    path('products/', shop_views.product_list, name='product_list'),
    path('product/<int:id>/', shop_views.product_detail, name='product_detail'),
    path('purchase_request/', shop_views.purchase_request, name='purchase_request'),
    path('my_requests/', shop_views.my_requests, name='my_requests'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='products/', permanent=False), name='index'),  # Redirect root URL to product list
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
]
