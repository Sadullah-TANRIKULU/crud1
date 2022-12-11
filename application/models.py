from django.db import models

# Create your models here.


class Todo(models.Model):
    todo_name = models.CharField(max_length=100)


class Task(models.Model):
    task_name = models.CharField(max_length=100)

#  create / insert / add - POST
#  retreive / fetch - GET
#  update / edit - PUT
#  delete / remove - DELETE
