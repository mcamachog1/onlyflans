
from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormForm


# Create your views here.
def index(request):  #Welcome
    return render(request, 'web/index.html')
def about(request):
    return render(request, 'web/about.html')
def welcome(request):
    return render(request, 'web/welcome.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormForm()
    return render(request, 'web/contacto.html',{'form':form})

def exito(request):
    return render(request, 'web/exito.html', {})
