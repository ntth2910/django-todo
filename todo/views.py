from django.http import HttpResponse
from django.shortcuts import redirect, render

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
