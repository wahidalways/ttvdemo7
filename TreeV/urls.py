from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('products', products, name='products'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]