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
        formpillow = pillowForms()
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
        answer = request.POST.get("люблю")
        if answer != "Беларусь":
            return HttpResponse(f"<h3>Любiць  {answer} вельмi добра, але ж гэта не верны адказ, мабуць табе сюды i не трыба заходзiць!</h3>")
        else:
            return render(request, 'kkbchb.html')

    else:
        form = answerForms()
        return render(request, 'nopasaran.html',{"form": answerForms})

def orderPage(request):
    return render(request, 'order.html')

def orderPage(request):
    if request.method == "POST":
        id = request.GET.get ("Продукт")
        name = request.GET.get ("Имя")
        Email = request.POST.get("Email")
        телефон = request.POST.get("телефон")
        print = request.POST.get("Принт")
        return HttpResponse(f"<p>Hello {name} ur age is {Email}</p>")


    else:
        formorder = orderForms()
        return render(request, 'order.html',{'formorder': orderForms})