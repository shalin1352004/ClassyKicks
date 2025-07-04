from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # Import this

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')  # ✅ changed from ImageField to CloudinaryField

# Optional: move this view to `views.py` if it’s not a model
from django.shortcuts import render

def contact(request):
    whatsapp_number = '918238322005'
    return render(request, 'store/contact.html', {'whatsapp_number': whatsapp_number})
