from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def products(request):
    return render(request, 'products.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')