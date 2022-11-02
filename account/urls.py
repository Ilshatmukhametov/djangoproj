from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index ),
    path('logoutUser',views.logoutUser),
    path('updateAuto', views.UpdateAuto, name='updateAuto')
]