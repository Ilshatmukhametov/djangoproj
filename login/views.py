from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages



def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print()
            return redirect('/account/')
        else:
            messages.info(request, 'Логин или пароль неверны')

    context = {}
    return render(request, 'main/Вход.html')
