from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from djangoProject import decorators
from djangoProject.decorators import allowed_users

from .models import User, History
from main.models import Auto, Docs
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from django.contrib import messages
from .forms import UpdateUserForm, UpdateAutoForm, UpdateDocsForm

@login_required(login_url='login')
def index(request):
    repairs = History.objects.filter(user=request.user.user).order_by('id')
    forma = UpdateAutoForm(instance=Auto.objects.get(user=request.user.user.user))
    form = UpdateUserForm(instance=User.objects.get(user=request.user.user.user))
    formDocs = UpdateDocsForm(instance=Docs.objects.get(user=request.user.user.user))
    if request.method == "POST":
        if request.POST.get('user'):
            form = UpdateUserForm(request.POST, instance=User.objects.get(user=request.user.user.user))
            if form.is_valid():
                form.save()
        if request.POST.get('car'):
            forma = UpdateAutoForm(request.POST, instance=Auto.objects.get(user=request.user.auto.user))
            if forma.is_valid():
                forma.save()
        if request.POST.get('docs'):
            formDocs = UpdateDocsForm(request.POST, instance=Docs.objects.get(user=request.user.user.user))
            if formDocs.is_valid():
                formDocs.save()
        if request.POST.get('repair'):
            History.objects.create(user=request.user.user ,name=request.user.user.name,phone_number=request.user.user.number, email=request.user.user.email, year=request.user.auto.year, vin=request.user.auto.vin, model= request.user.auto.model, address=request.POST.get('address'), data=request.POST.get('date'), timedate=request.POST.get('time'), problem=request.POST.get('problem'))
        if request.POST.get('repairAnother'):
            History.objects.create(user=request.user.user ,name=request.POST.get('nameAnother'),phone_number=request.POST.get('phoneAnother'), email=request.POST.get('emailAnother'), year=request.POST.get('yearAnother'), vin=request.POST.get('vinAnother'), model= request.POST.get('modelAnother'), address=request.POST.get('addressAnother'), data=request.POST.get('dateAnother'), timedate=request.POST.get('timeAnother'), problem=request.POST.get('problemAnother'))
            print('awdasd')
        return redirect('/account/')
    cars = Auto.objects.filter(user=request.user.user.user).all()
    orders = User.objects.filter(user=request.user.user.user).all()
    context={'orders': orders, 'form': form, 'forma': forma, 'formDocs': formDocs, 'repairs': repairs, 'cars': cars}
    return render(request, 'main/Личный кабинет.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login/')

def UpdateUser(request):
    form = UpdateUserForm(instance=User.objects.get(user=request.user.user.user))
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=User.objects.get(user=request.user.user.user))
        if form.is_valid():
            form.save()
            return redirect('/')

def UpdateAuto(request):
    formAuto = UpdateAutoForm(instance=Auto.objects.get(user=request.user.auto.user))
    if request.method == 'POST':
        formAuto = UpdateAutoForm(request.POST, instance=Auto.objects.get(user=request.user.auto.user))
        if formAuto.is_valid():
            formAuto.save()
            return redirect('/account/')
    return redirect('/account/')











