from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html')


def ulogin(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['msg'] = 'Login Failed Due to invalid username or password'
    return render(request, 'login.html', context)


def ulogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')


def uregister(request):
    context = {}
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        passwd = data.get('passw')
        rpasswd = data.get('rpassw')
        print(username)
        if passwd == rpasswd:
            user, created = User.objects.get_or_create(username=username)
        else:
            context['msg'] = 'Repeat Password Does not match'
        if created:
            passwd = data.get('password')
            user.set_password(passwd)
            user.email = data.get('email')
            user.save()
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'register.html', context)


def quiz(request, id):
    
    return render(request, 'quiz.html')


def leaderboard(request, id):
    return render(request, 'leaderboard.html')
