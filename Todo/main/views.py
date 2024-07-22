from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    #this function is created to add the tasks completed and incompleted into 2 variables
    t = Todo.objects.filter(completed=False)
    p = Todo.objects.filter(completed=True)
    context={
        'incomplete_todo':t,
        'complete_todo':p
    }
    return render(request,'home.html',context)

def add_task(request):
    if request.method=='POST':
        
        task = request.POST.get('task')
        t=Todo.objects.create(task=task)
        t.save()
        return redirect('home')
   
def mark_as_done(request,task_id):
    task = Todo.objects.get(id=task_id)
    task.completed=True
    task.save()
    return redirect('home')

def update_task(request,update_id):
    task= Todo.objects.get(id=update_id)
    if request.method =='POST':
        new_task=request.POST.get('new_task')
        task.task = new_task 
        task.save()
        return redirect('home')
    context={
            'task':task
        }
    return render(request,'update.html',context)

def delete_task(request,delete_id):
    task=Todo.objects.get(id=delete_id)
    task.delete()
    return redirect('home')

def mark_as_undone(request,task_id):
    task = Todo.objects.get(id=task_id)
    task.completed=False
    task.save()
    return redirect('home')
