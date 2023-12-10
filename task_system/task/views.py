from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'add_task.html', {'form': form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id) 
    task.delete()
    return redirect('home')



