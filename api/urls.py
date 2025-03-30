from django.contrib import admin
from django.urls import path, include
from .views import CustomTaskListView, CreateView, DetailView, UpdateView, DeleteView


urlpatterns = [
    path("tasks/", CustomTaskListView.as_view(), name="tasks"),
    path("tasks/create", CreateView.as_view(), name="tasks-create"),
    path("tasks/retrieve/<pk>/", DetailView.as_view(), name="task-create"),
    path("task/update/<pk>/", UpdateView.as_view(), name="task-update"),
    path("task/delete/<pk>/", DeleteView.as_view(), name="task-delete"),
]
