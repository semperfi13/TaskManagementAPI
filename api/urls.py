from django.urls import path
from .views import (
    CustomTaskListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("tasks/", CustomTaskListView.as_view(), name="tasks"),
    path("tasks/create", CreateView.as_view(), name="tasks-create"),
    path("tasks/retrieve/<pk>/", DetailView.as_view(), name="task-create"),
    path("task/update/<pk>/", UpdateView.as_view(), name="task-update"),
    path("task/delete/<pk>/", DeleteView.as_view(), name="task-delete"),
]
