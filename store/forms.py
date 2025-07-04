# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, ProductImage, Brand

# === Product Form ===
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand', 'name', 'description', 'price']
        widgets = {
            'brand': forms.Select(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300 focus:outline-none'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300',
                'placeholder': 'Enter product description',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300',
                'placeholder': 'Enter price'
            }),
        }

# === Product Image Form (Cloudinary Compatible) ===
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'multiple': True,
                'class': 'w-full p-2 bg-white border border-gray-300 rounded-md'
            })
        }

# === Brand Form ===
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300',
                'placeholder': 'Enter brand name'
            }),
        }

# === Custom Login Form with Tailwind Styling ===
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 rounded-md bg-white text-black border border-pink-300 focus:outline-none focus:ring-2 focus:ring-pink-400',
            'placeholder': 'Enter username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full p-2 rounded-md bg-white text-black border border-pink-300 focus:outline-none focus:ring-2 focus:ring-pink-400',
            'placeholder': 'Enter password'
        })
