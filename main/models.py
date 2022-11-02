from django.db import models
from django.contrib.auth.models import User


class Auto(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    vin = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)
# Create your models here.

class Docs(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=200, null=True)
    ctc = models.CharField(max_length=200, null=True)
    policy = models.CharField(max_length=200, null=True)
    license = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.user)


class TestTable(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    test1 = models.CharField(max_length=200, null=True)
    test2 = models.CharField(max_length=200, null=True)
    test3 = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.user)