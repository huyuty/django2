from django.contrib import admin
from django.urls import path

from product.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('check-out/', CheckView.as_view(), name='check-out'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart')
]
