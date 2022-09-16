from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "main/index.html", {'title':'Список всех задач', 'tasks':tasks})

def about(request):
    return render(request, "main/about.html")

def create(request):
    form = TaskForm()
    content = {
        'form': form
    }
    return render(request, "main/create.html")