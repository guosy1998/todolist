from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import redirect

from .models import Todolist
from .serializer import TodolistSerializer

# Create your views here.
class TodolistView(APIView):

    # show the items by certain order
    def show(request):
        seq = request.POST.get('seq')

        # 3 options for seq: 2:expire_date; 1:priority; 0:id
        if seq == '2':
            todolist = Todolist.objects.all().order_by('expire_date')
        elif seq == '1':
            todolist = Todolist.objects.all().order_by('-priority')
        else:
            todolist = Todolist.objects.all().order_by('id')

        serializer = TodolistSerializer(todolist, many=True)
        return render(request, template_name='todolist.html', context={'todolist': serializer.data})

    # create a new item
    def add(request):
        serializer = TodolistSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
        return redirect('todolist')

    # delete an existing item
    def delete(request):
        id = request.POST.get('id')
        item = Todolist.objects.get(id=id)
        item.delete()
        return redirect('todolist')

    # change the status of an existing item
    def status(request):
        id = request.POST.get('id')
        item = Todolist.objects.get(id=id)
        item.status = '1'
        item.save()
        return redirect('todolist')

    # edit an existing item, showing the edit page
    def edit(request):
        id = request.POST.get('id')
        todolist = Todolist.objects.filter(id=id)
        serializer = TodolistSerializer(todolist, many=True)
        return render(request, template_name='todolist_edit.html', context={'todolist': serializer.data})

    # edit an existing item, submit the result
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
    # Django restframework example code, not used
    # Add the following lines when needed
    # from rest_framework import status, generics
    # from rest_framework.response import Response
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
