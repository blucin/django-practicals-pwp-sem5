from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fileForm/', views.fileForm, name='fileForm'),
    path('fileFormData/', views.fileFormData, name='fileFormData'),
]