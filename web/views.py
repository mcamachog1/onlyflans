from django.shortcuts import render


# Create your views here.
def index(request):  #Welcome
    return render(request, 'web/index.html')
def about(request):
    return render(request, 'web/about.html')
def home(request):
    return render(request, 'web/home.html')