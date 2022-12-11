from rest_framework import viewsets
from . import models
from . import serializers

class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer # use this serializer to json conversion

class TaskViewset(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

#  list(), retrieve(), create(), update(), destroy()