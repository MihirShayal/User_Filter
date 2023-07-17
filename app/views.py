from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'data':'Hai Mihir'}
    return render(request,'usdf.html',d)