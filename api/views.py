from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as Filters
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import Http404


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


"""Task Management (CRUD)"""


def get_object(pk, request):
    try:
        return Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        raise Http404


class ListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = TaskFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["status", "priority", "due_date"]
    ordering_fields = ["priority", "due_date"]
    ordering = ["status", "priority", "due_date"]

    def get(self, request):
        # title = request.query_params.get("title", "")

        tasks = Task.objects.filter(user=self.request.user)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class CreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class DetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        task = get_object(pk, request)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class UpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        task = get_object(pk, request)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        task = get_object(pk, request)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" USER LOGIN, vREGISTER AND LOGOUT API VIEW"""


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        try:
            user = get_object_or_404(User, username=request.data["username"])

            if not user.check_password(request.data["password"]):
                return Response(
                    {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(instance=user)
            return Response({"token": token.key, "user": serializer.data})
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["POST"])
def register(request):
    if request.method == "POST":
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(username=request.data["username"])
                user.set_password(request.data["password"])
                user.save()
                token = Token.objects.create(user=user)
                return Response({"token": token.key, "user": serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def logout(request):
    if request.method == "POST":
        try:
            request.user.auth_token.delete()
            return Response(
                {"message": f"Successfully logged {request.user.username} out."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
