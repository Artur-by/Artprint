from django.shortcuts import render


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
    return render(request, 'zakaz6.html')

def puzzlesPage(request):
    return render(request, 'zakaz7.html')

def photoPage(request):
    return render(request, 'zakaz8.html')

def glassPage(request):
    return render(request, 'zakaz9.html')

def magnitPage(request):
    return render(request, 'zakaz10.html')