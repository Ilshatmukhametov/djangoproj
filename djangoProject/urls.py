from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('account/', include('account.urls')),
    path('login/',include('login.urls')),
    path('price/', include('price.urls')),
    path('recovery/',include('recovery.urls')),
    path('signup/', include('signup.urls')),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('update/', views.UpdateAuto, name='updateAuto')

]
