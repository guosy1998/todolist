"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', views.TodolistView.show, name='todolist'),
    path('todolist/add', views.TodolistView.add, name='add'),
    path('todolist/delete', views.TodolistView.delete, name='delete'),
    path('todolist/status', views.TodolistView.status, name='status'),
    path('todolist/edit', views.TodolistView.edit, name='edit'),
    path('todolist/edit_submit', views.TodolistView.edit_submit, name='edit_submit'),
]
