from django.shortcuts import render


# Create your views here.
def index(request):  #Welcome
    return render(request, 'web/index.html')
def about(request):
    return render(request, 'web/about.html')
def welcome(request):
    return render(request, 'web/welcome.html')

def contacto(requests):
    return render(requests, 'web/contacto.html')