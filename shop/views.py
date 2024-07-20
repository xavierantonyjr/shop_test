from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, PurchaseRequest

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
    return render(request, 'shop/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def purchase_request(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = Product.objects.get(id=product_id)
        PurchaseRequest.objects.create(product=product, customer=request.user)
        return redirect('my_requests')
    return redirect('product_list')

@login_required
def my_requests(request):
    requests = PurchaseRequest.objects.filter(customer=request.user)
    return render(request, 'shop/my_requests.html', {'requests': requests})
