from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages


# Create your views here.
def products(request):
    return render(request, 'products/products.html')


def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully')
            return redirect('add-products-url')
        else:
            messages.error(request, 'Product saving failed')
            return redirect('add-products-url')
    else:
        form = ProductForm()
    return render(request, 'products/add-products.html', {'form': form})


def update_products(request):
    return render(request, 'products/update-products.html')

