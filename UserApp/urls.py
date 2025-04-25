from django.contrib import admin
from django.urls import path
from Login import views as Login_Views
from Menu import views as Menu_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login_Views.login, name='login'),
    path('menu/', Menu_Views.Menu, name='menu'),
    path('', Login_Views.login, name='default'),
]
