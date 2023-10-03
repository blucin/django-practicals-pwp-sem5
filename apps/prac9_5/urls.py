from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('login/', views.login, name='login'),
    path('loginSuccess/', views.loginSuccess, name='loginSuccess'),
    path('loginFail/', views.loginFail, name='loginFail'),
]