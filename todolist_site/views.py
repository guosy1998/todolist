from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from .models import Todolist
from .serializer import TodolistSerializer

# Create your views here.
class TodolistView(APIView):

    def show(request):
        todolist = Todolist.objects.all().order_by('id')
        serializer = TodolistSerializer(todolist, many=True)
        return render(request, template_name='todolist.html', context={'todolist': serializer.data})

    def add(request):
        serializer = TodolistSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
        return redirect('todolist')

    def delete(request):
        id = request.POST.get('id')
        item = Todolist.objects.get(id=id)
        item.delete()
        return redirect('todolist')

    def status(request):
        id = request.POST.get('id')
        item = Todolist.objects.get(id=id)
        item.status = '1'
        item.save()
        return redirect('todolist')

    def edit(request):
        id = request.POST.get('id')
        todolist = Todolist.objects.filter(id=id)
        serializer = TodolistSerializer(todolist, many=True)
        return render(request, template_name='todolist_edit.html', context={'todolist': serializer.data})

    def edit_submit(request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        content = request.POST.get('content')
        expire_date = request.POST.get('expire_date')
        status = request.POST.get('status')
        priority = request.POST.get('priority')

        item = Todolist.objects.get(id=id)
        item.name = name
        item.content = content
        item.expire_date = expire_date
        item.status = status
        item.priority = priority
        item.save()

        return redirect('todolist')

"""
    def get(self, request, format=None):
        todolist = Todolist.objects.all()
        serializer = TodolistSerializer(todolist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
