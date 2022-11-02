from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import send_mail


def index(request):
    if request.method == "POST":
        if request.POST.get('send_email'):
            subject = 'Заказ расчета стоимости!'
            message = 'VIN: ' + request.POST.get('vin') + '\n Модель: ' + request.POST.get('model') + '\n Год изготовления: ' + request.POST.get('year') + '\n Контакты для связи: ' + request.POST.get('email') + '\n Услуга: ' + request.POST.get('service')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['servicezazhiganie@mail.ru']
            send_mail(subject, message, email_from, recipient_list)
            redirect('/price/')
    return render(request, 'main/Виды работ.html')



def send_msg(request):
    subject = 'Новая заявка!'
    message = request.POST.get('name_vin')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['servicezazhiganie@mail.ru', ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Successful")
