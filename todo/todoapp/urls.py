from django.urls import path
from .views  import TodoList


urlspatterns = [
    path('todo/', TodoList.as_view(), name='todo-list'),
]