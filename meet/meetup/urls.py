from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manager', views.manager, name='manager'),
    path('employee', views.employee, name='employee'),
    path("update/<int:id>/", views.update_task, name="update_task")
]