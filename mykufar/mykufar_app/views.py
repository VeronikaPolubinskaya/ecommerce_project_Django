from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# from .forms import NewProductForm, EditProductForm, SignupForm, ProductFilterForm
from item.models import Category, Item
# from rest_framework import viewsets
# from rest_framework.permissions import AllowAny
# from .serializers import CategorySerializer, ProductSerializer
# from django.contrib.auth.models import User
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html',{
        'form':form
    })

