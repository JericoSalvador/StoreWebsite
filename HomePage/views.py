from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Review 

# Create your views here.

def index(request): 
    context = {
        'items': Item.objects.all()
    }
    return render(request, "ItemList.html", context)

class ShoppingView(ListView): 
    model = Item
    template_name = 'ItemList.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = "ItemDetail.html"

class ReviewView(ListView): 
    model = Review
    template_name = "ReviewView.html"
    
def ReviewPage(request, itemslug): 
    context = {
        'item': Item.objects.filter(slug=itemslug)[0],
        'reviews': Review.objects.filter(item__slug=itemslug)
    }
    return render(request, 'ReviewPage.html', context)
