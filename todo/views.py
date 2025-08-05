from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Task

# Create your views here.
def addTask(request):
    # Logic to add a task

    # this is secure way to get data from POST request
    # task = request.POST.get('task')

    task = request.POST['task']
    Task.objects.create(task=task)

    # this is an insecure way to get data from POST request
    # tas = request.POST['task']  # This will raise an error if 'task' is not in POST data

    return redirect('home')

def markTaskAsDone(request, id):
    # Logic to mark a task as done
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()

    return redirect('home')

def markTaskAsUnDone(request, id):
    # Logic to mark a task as undone
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()

    return redirect('home')

def deleteTask(request, id):
    # Logic to delete a task
    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect('home')
def editTask(request, id):
    # Logic to edit a task
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
       newTask = request.POST['task']
       task.task = newTask
       task.save()
       return redirect('home')
    else :
        context = {
            'task': task,
        }
        return render(request, 'edit_task.html', context)
