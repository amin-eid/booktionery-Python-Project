from django.shortcuts import render,redirect
from . import models


def index(request):
    return render(request,'register.html')

def root(request):
    context = models.registered()
    return render(request,'register.html',context)

def registration(request):
    if request.method =='POST':
        user = models.register(request.POST)
        if user:
            if 'id' not in request.session:
                request.session['id'] = user['id']
            return redirect('/success')
        else:
            return redirect('/')
    return redirect('/')
