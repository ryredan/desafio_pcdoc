from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/ajax/paciente', views.get_pacientes, name="get_pacientes"),
    path('post/ajax/paciente', views.post_paciente, name = "post_paciente"),
    path('delete/ajax/paciente', views.delete_paciente, name = "delete_paciente"),
]