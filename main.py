from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoriesView(TemplateView):
    template_name = 'categories.html'


class CheckView(TemplateView):
    template_name = 'check-out.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ProductView(TemplateView):
    template_name = 'product-page.html'


class CartView(TemplateView):
    template_name = 'shopping-cart.html'
