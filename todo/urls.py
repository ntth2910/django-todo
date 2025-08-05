
from django.urls import path

from todo import views



urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markTaskAsDone/<int:id>/', views.markTaskAsDone, name='markTaskAsDone'),
    path('markTaskAsUnDone/<int:id>/', views.markTaskAsUnDone, name='markTaskAsUnDone'),
    path('deleteTask/<int:id>/', views.deleteTask, name='deleteTask'),
    path('editTask/<int:id>/', views.editTask, name='editTask'),
]