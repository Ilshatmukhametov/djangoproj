from django.contrib.auth.models import User, AbstractUser
from django.db import models

class User(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    birth = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.user)
# Create your models here.


class History(models.Model):
    STATUS = (
        ('Принято в ремонт', "Принято в ремонт"),
        ('Выполняется ремонт', "Выполняется ремонт"),
        ('Ремонт выполнен', "Ремонт выполнен"),
        ('Заявка закрыта', "Заявка закрыта"),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, verbose_name='Имя', blank=True)
    phone_number = models.CharField(max_length=200, null=True, verbose_name='Номер телефона', blank=True)
    email = models.CharField(max_length=200, null=True, verbose_name='Почта', blank=True)
    year = models.CharField(max_length=200, null=True, verbose_name='Год выпуска', blank=True)
    vin = models.CharField(max_length=200, null=True, verbose_name='ВИН', blank=True)
    model = models.CharField(max_length=200, null=True, verbose_name='Модель и марка', blank=True)
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес', blank=True)
    data = models.CharField(max_length=200, null=False, verbose_name='Дата', blank=True)
    timedate = models.CharField(max_length=200, null=True, verbose_name='Время', blank=True)
    problem = models.CharField(max_length=200, null=True, verbose_name='Проблема', blank=True)
    adminComm = models.CharField(max_length=200, null=True, verbose_name='Комментарий админа', blank=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True, verbose_name='Статус', blank=True)

    def __str__(self):
        return f'Логин: {self.user}|  Имя: {self.name}|  Модель: {self.model}|  Статус: {self.status}'