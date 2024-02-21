from django.shortcuts import render
from .models import Publi
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def feed_page(request):
    publis = Publi.objects.all()[::-1]
    return render(request, "feed.html", {
        'publis' : publis
    })


def publicate_page(request):
    if request.method == 'GET':
        return render(request, "publicate.html")
    elif request.method == 'POST':
        autor = request.POST.get('autor')
        data = datetime.today()
        conteudo = request.POST.get('conteudo')
        publi = Publi()
        publi.autor = autor
        publi.data = data
        publi.conteudo = conteudo
        publi.save()
        return HttpResponseRedirect('/feed')
    else:
        return HttpResponseBadRequest()

def signup_page(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        login(request, user)
        return HttpResponseRedirect('/user')
    else:
        return HttpResponseBadRequest()
    
@login_required(login_url='/login')
def user_page(request):
    return render(request, 'user.html', {
        'username': request.user.username
    })

@login_required(login_url='/login')
def logout_page(request):
    return HttpResponseRedirect('/login')

def login_page(request):
    if request.method == 'GET':
        return render(request, "login.html", {
            'incorrect_login': False 
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user')
        else:
            return render(request, 'login.html', {
                'incorrect_login': True 
            })
    else:
        return HttpResponseBadRequest()