from django.shortcuts import render ,redirect
from django.http import HttpResponse
from item.models import Category, Item
from .forms import Signupform
# Create your views here.

def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'contact.html')

def sighup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:        
        form = Signupform


    return render(request, 'signup.html',{
        'form': form
    })

