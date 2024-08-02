# shop/views.py
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Request
from .forms import ProductForm, RequestForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'shop/home.html')


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

# shop/views.py


def purchase_request(request):
    # Your view logic here
    return render(request, 'shop/purchase_request.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def approve_request(request, id):
    req = get_object_or_404(Request, id=id)
    if request.method == 'POST':
        req.approve()
        return redirect('list_requests')
    return render(request, 'shop/approve_request.html', {'request': req})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'shop/delete_product.html', {'product': product})

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/edit_product.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'shop/list_products.html', {'products': products})

def list_requests(request):
    requests = Request.objects.all()
    return render(request, 'shop/list_requests.html', {'requests': requests})

def list_my_requests(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'shop/list_my_requests.html', {'requests': requests})

def login_view(request):
    # Your login logic here
    return render(request, 'shop/login.html')

# your logout logic here
def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            next_url = request.GET.get('next', reverse('product_list'))
            return redirect(next_url)
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def send_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_my_requests')
    else:
        form = RequestForm()
    return render(request, 'shop/send_request.html', {'form': form})
