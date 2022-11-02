from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from account.models import User
from main.models import Auto, Docs
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from django.contrib import messages



def index(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            User.objects.create(user=user, email=user.email)
            Auto.objects.create(user=user)
            Docs.objects.create(user=user)
            return redirect('/login/')
        else:
            errors = form.errors
            messages.info(request, errors)
            print(form.errors)
    return render(request, 'main/Регистрация.html', context)


