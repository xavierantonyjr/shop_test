# shop/models.py

from django.db import models
from django.contrib.auth.models import User


class PurchaseRequest(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    # other fields...

    def __str__(self):
        return self.product

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Request(models.Model):
    PENDING = 'P'
    APPROVED = 'A'
    REJECTED = 'R'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        self.status = self.APPROVED
        self.save()

    def reject(self):
        self.status = self.REJECTED
        self.save()

    def __str__(self):
        return f"Request for {self.product.name} by {self.user.username}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
