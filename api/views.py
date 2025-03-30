from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as Filters
from rest_framework import filters


class TaskFilter(Filters.FilterSet):
    PRIORITY_CHOICES = [("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    STATUS_CHOICES = [("Pending", "Pending"), ("Completed", "Completed")]
    due_date = Filters.DateFilter()
    priority = Filters.CharFilter(
        max_length=25, choices=PRIORITY_CHOICES, default="Medium"
    )
    status = Filters.CharFilter(
        max_length=25, choices=STATUS_CHOICES, default="Pending"
    )

    class Meta:
        model = Task
        fields = ["status", "priority", "due_date"]


class CustomTaskListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["status", "priority", "due_date"]
    ordering_fields = ["priority", "due_date"]
    ordering = ["status", "priority", "due_date"]


class CreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class DetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class UpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class DeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
