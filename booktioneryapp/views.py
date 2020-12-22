from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,'index.html')

from django.shortcuts import render, HttpResponse
def register(request):
    return render(request,'register.html')
    