from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib.auth.views import LoginView

from .models import Product, ProductImage, Brand
from .forms import ProductForm, ProductImageForm, LoginForm, BrandForm

# === Product List View ===
def product_list(request):
    brand_id = request.GET.get('brand')
    products = Product.objects.filter(brand_id=brand_id) if brand_id else Product.objects.all()
    brands = Brand.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'brands': brands,
    })

# === Product Detail View ===
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# === Custom Login View ===
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

# === Add Product View ===
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

# === Add Brand View ===
@login_required
def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = BrandForm()
    return render(request, 'store/add_brand.html', {'form': form})

# === Contact View ===
def contact(request):
    whatsapp_number = '918238322005'
    return render(request, 'store/contact.html', {'whatsapp_number': whatsapp_number})
