from application.viewsets import TodoViewset, TaskViewset
from rest_framework import routers

todo_router = routers.DefaultRouter()
todo_router.register('todo', TodoViewset)

task_router = routers.DefaultRouter()
task_router.register('task', TaskViewset)


#  localhost:port/api/
# GET, list() -> api/todo or retrieve() -> api/todo/id
# POST, 
# PUT, 
# DELETE