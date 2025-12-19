from multiprocessing import context #import context is done by me 
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': "this is variable passed from views.py to index.html"
    }
    return render(request, 'index.html', context)
    # # return HttpResponse("this is homepage")

def about(request):
     return render(request, 'about.html')

def contactUS(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def service1(request):
    return render(request, 'service1.html')

def service2(request):
    return render(request, 'service2.html')

def service3(request):
    return render(request, 'service3.html')

def payment_Plans(request):
    return render(request, 'payment_Plans.html')