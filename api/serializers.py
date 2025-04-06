from rest_framework import serializers
from .models import Task
import datetime
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["user"]

    def validate_due_date(self, data):
        today = datetime.date.today()
        # year = d.strftime("%Y")
        if data < today:
            raise serializers.ValidationError("The due date must be in the future.")
        return data


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta(object):
        model = User
        fields = ["id", "username", "password", "email"]
