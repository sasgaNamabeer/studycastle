from django.shortcuts import render
import scapp.views
# Create your views here.

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def blogsingle(request):
    return render(request, 'blog-single.html')