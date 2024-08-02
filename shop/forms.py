from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PurchaseRequest
from .models import UserProfile

# shop/forms.py

from django import forms
from .models import Product, Request

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['product', 'quantity']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = UserProfile(user=user, phone_number=self.cleaned_data['phone_number'])
            profile.save()
        return user
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')


class PurchaseRequestForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequest
        fields = ['product', 'quantity']


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PurchaseRequestForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequest
        fields = ['product', 'quantity']
