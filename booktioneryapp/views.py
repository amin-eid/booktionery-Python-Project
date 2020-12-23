from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def user(request):
    return render(request,'user.html')

def thanks(request):
    return render(request,'thankyou.html')

def admin2(request):
    return render(request,'adminorders.html')
def admin3(request):
    return render(request,'adminusers.html')
def admin4(request):
    return render(request,'adminproducts.html')