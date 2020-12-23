from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,'main.html')


def register(request):
    return render(request,'register.html')
