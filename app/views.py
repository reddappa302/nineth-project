from django.shortcuts import render

# Create your views here.

def red(request):
    return render(request,'red.html')

def black(request):
    return render(request,'black.html')     
