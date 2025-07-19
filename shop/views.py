from django.shortcuts import render , get_object_or_404
from shop.models import Product , Category

# Create your views here.
def home_view(request):
    return render(request , 'index.html')

def product_view(request , pk):
    item = get_object_or_404( Product , pk=pk )
    context = {
        'item':item ,
    }
    return render(request , 'product.html', context)

def products_view(request):
    item = Product.objects.all()
    category = Category.objects.all()
    context = {
        'item':item,
        'category':category,
    }
    return render(request , 'products.html', context)