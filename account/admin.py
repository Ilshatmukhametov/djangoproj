from django.contrib import admin
from .models import User, History
from main.models import Auto, Docs
# Register your models here.

admin.site.register(User)
admin.site.register(Auto)
admin.site.register(Docs)

admin.site.register(History)

