from django.shortcuts import render
from product.models import *

from django.views.generic import TemplateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoriesView(ListView):
    model = Product
    template_name = 'categories.html'


class CheckView(TemplateView):
    template_name = 'check-out.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ProductView(DetailView):
    model = Product
    template_name = 'product-page.html'


class CartView(TemplateView):
    template_name = 'shopping-cart.html'

