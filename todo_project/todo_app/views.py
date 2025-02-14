from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# **1️⃣ Create & List To-Do Items**
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# **2️⃣ Retrieve, Update & Delete a To-Do**
class TodoRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def home(request):
    return render(request, "todo_app/home.html")

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo_app/todo_list.html", {"todos": todos})

def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
    else:
        form = TodoForm()
    return render(request, "todo_app/todo_form.html", {"form": form, "title": "Create To-Do"})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todo_app/todo_form.html", {"form": form, "title": "Update To-Do"})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("todo-list")
    return render(request, "todo_app/todo_delete.html", {"todo": todo})
