from rest_framework import serializers
from .models import Task
import datetime


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_due_date(self, data):
        today = datetime.date.today()
        # year = d.strftime("%Y")
        if data < today:

            raise serializers.ValidationError("The due date must be in the future.")
        return data
