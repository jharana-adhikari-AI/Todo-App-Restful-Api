from django.urls import path
from .views import home, todo_list, todo_create, todo_update, todo_delete

urlpatterns = [
    path("", home, name="home"),
    path("todos/", todo_list, name="todo-list"),
    path("todos/create/", todo_create, name="todo-create"),
    path("todos/update/<int:pk>/", todo_update, name="todo-update"),
    path("todos/delete/<int:pk>/", todo_delete, name="todo-delete"),
]
