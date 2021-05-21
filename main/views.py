from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from.models import *

# Create your views here.

def artprintPage(request):
    return render(request, 'artprint.html')

def zakazPage(request):
    return render(request, 'zakaz.html')

def futbPage(request):
    return render(request, 'zakaz1.html')

def sweatPage(request):
    return render(request, 'zakaz2.html')

def tolstPage(request):
    return render(request, 'zakaz3.html')

def apronPage(request):
    return render(request, 'zakaz4.html')

def shopperPage(request):
    return render(request, 'zakaz5.html')

def pillowPage(request):
    if request.method == "POST":
        #colorprice = request.GET.get ("Размер")
        #sizeprice = request.GET.get ("Формат" )
        #size = request.POST.get("Размер")
        #ide = request.POST.get("Формат")

        #formpillow = pillowForms()
        value = 10
        return  render(request, 'zakaz6.html', {'value': value})
    else:
        formpillow=pillowForms()
        return render(request, 'zakaz6.html',{'formpillow': formpillow})

def puzzlesPage(request):
    return render(request, 'zakaz7.html')

def photoPage(request):
    return render(request, 'zakaz8.html')

def glassPage(request):
    return render(request, 'zakaz9.html')

def magnitPage(request):
    return render(request, 'zakaz10.html')

def nopasaranPage(request):
    if request.method == "POST":

        return  render(request, 'zakaz/zakaz6.html')
    else:
        form = answerForms()
        return render(request, 'nopasaran.html')