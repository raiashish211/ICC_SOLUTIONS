from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})
def about(request):
    return render(request, 'myapp/about.html')
def products(request):
    return render(request, 'myapp/products.html')