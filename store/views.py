from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, ProductImage, Brand
from .forms import ProductForm, ProductImageForm
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from django.shortcuts import render
from .models import Product, Brand

def product_list(request):
    brand_id = request.GET.get('brand')
    
    # Filter products based on brand
    if brand_id:
        products = Product.objects.filter(brand_id=brand_id)
    else:
        products = Product.objects.all()
    
    brands = Brand.objects.all()
    
    return render(request, 'store/product_list.html', {
        'products': products,
        'brands': brands,
    })

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})
from .forms import LoginForm
from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LoginView
from .forms import LoginForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


@login_required
def add_product(request):
    ImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=5, max_num=5, can_delete=True)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())
        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            for image_form in formset:
                if image_form.cleaned_data:
                    image = image_form.save(commit=False)
                    image.product = product
                    image.save()
            return redirect('product_list')
    else:
        form = ProductForm()
        formset = ImageFormSet(queryset=ProductImage.objects.none())
    return render(request, 'store/add_product.html', {'form': form, 'formset': formset})
from .forms import BrandForm
from django.contrib.auth.decorators import login_required

@login_required
def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')  # or redirect to 'product_list'
    else:
        form = BrandForm()
    return render(request, 'store/add_brand.html', {'form': form})
