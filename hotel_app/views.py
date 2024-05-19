from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Gallary
from .forms import CreatProduct

def home(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html', context={"product":product, "category":category})


def category(request, id):
    category = get_object_or_404(Category, id=id)
    product = category.product.all()
    category = Category.objects.all()
    return render(request, 'home.html', context={"product":product, "category":category})


def batafsil(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'batafsil.html', context={"product":product})


def about(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'about.html', context={"category":category})



def gallary(request):
    product = Product.objects.all()
    category = Category.objects.all()
    image = Gallary.objects.all()
    return render(request, 'gallary.html', context={"image":image, "product":product, "category":category})



def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/')


def create_product(request):
    form=CreatProduct()
    if request.method == 'POST':
        form = CreatProduct(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('/')
    return render(request, 'create_product.html', context={"form": form})


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = CreatProduct(instance=product)
    if request.method == 'POST':
        form = CreatProduct(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_product.html', context={"form": form})