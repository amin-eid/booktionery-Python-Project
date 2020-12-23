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

from django.shortcuts import render, HttpResponse
def register(request):
    return render(request,'register.html')
    
>>>>>>> 42bcbba83cd2e946a226e9217c0ce1ec0ee17637
