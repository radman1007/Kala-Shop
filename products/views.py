from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import CommentForm

class ProductListView(ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context