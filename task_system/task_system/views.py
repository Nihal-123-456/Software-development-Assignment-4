from django.shortcuts import render
from task.models import *

def home(request):
    tasks = TaskModel.objects.all()
    return render(request, 'base.html', {'tasks': tasks})