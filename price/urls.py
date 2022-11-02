from django.urls import path
from . import  views
from .views import send_msg
urlpatterns = [
    path('',views.index ),
]