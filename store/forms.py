from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand', 'name', 'description', 'price']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {'image': forms.ClearableFileInput()}
from .models import Brand
from django import forms

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'}),
        }
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        # Add Tailwind classes to both fields
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 rounded-md bg-white text-black border border-pink-300 focus:outline-none focus:ring-2 focus:ring-pink-400',
            'placeholder': 'Enter username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full p-2 rounded-md bg-white text-black border border-pink-300 focus:outline-none focus:ring-2 focus:ring-pink-400',
            'placeholder': 'Enter password'
        })
