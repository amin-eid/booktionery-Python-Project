from django.shortcuts import render, HttpResponse

def index(request):
<<<<<<< HEAD
    return render(request,'main.html')


def register(request):
    return render(request,'register.html')

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
                    return redirect('/quotes')
    return redirect('/')
=======
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')
<<<<<<< HEAD

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
=======
    
>>>>>>> 42bcbba83cd2e946a226e9217c0ce1ec0ee17637
>>>>>>> 12b556b72a7873520cd0b60fc3ce4e8f8a1c6b0c
