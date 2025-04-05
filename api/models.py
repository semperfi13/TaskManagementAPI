from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    STATUS_CHOICES = [("Pending", "Pending"), ("Completed", "Completed")]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(
        max_length=25, choices=PRIORITY_CHOICES, default="Medium"
    )
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default="Pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return f"Task: {self.title}  by {self.user.username}"
