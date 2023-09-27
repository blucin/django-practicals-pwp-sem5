from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('formData/', views.formData, name='formData'),
]