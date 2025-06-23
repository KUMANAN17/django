from rest_framework import generics
from .models import Todoitems
from .serializes import todoSerializer 

class TodoList(generics. ListCreateAPIView):
    queryset = Todoitems.objects.all()
    serializer_class = todoSerializer
