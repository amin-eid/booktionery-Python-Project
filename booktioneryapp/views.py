from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from . import models



def root(request):
    if 'user_id' in request.session:
        redirect('/succes')
    return render(request,'main.html')

def reg(request):
    return render(request,'register.html')

def welcome(request):
    if 'user_id' in request.session:
        context = {
            'first_name':request.session['first_name'],
            'last_name':request.session['last_name'],
            'user_id':request.session['user_id'],
            'pos':'main',
        }
        return render(request,'main.html',context)
    return redirect('/')

def registration(request):
    if request.method =='POST':
        errors = models.reg_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.register(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/success')
        return redirect('/')


def login(request):
    if request.method=='POST':
        errors = models.login_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.login(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/success')
    return redirect('/')

def user_profile(request,id):
    if 'user_id' in request.session:
        context = {
            'first_name':request.session['first_name'],
            'last_name':request.session['last_name'],
            'user_id':request.session['user_id'],
            'pos':'my_profile',
        }
        return render(request,'user.html',context)


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
    return redirect('/')


