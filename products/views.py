from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class product_list_view(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'