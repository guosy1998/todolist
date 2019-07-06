from django.urls import path
from todolist_site import views

urlpatterns = [
    path('', views.TodolistView.show, name='todolist'),
    path('add', views.TodolistView.add, name='add'),
    path('delete', views.TodolistView.delete, name='delete'),
    path('status', views.TodolistView.status, name='status'),
    path('edit', views.TodolistView.edit, name='edit'),
]