#  api <--> mobile app / web app json/xml

from rest_framework import serializers
from .models import Todo, Task

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'  # to convert all model(db) fields or ('just one/two field')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

