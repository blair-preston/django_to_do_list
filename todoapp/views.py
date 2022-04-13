from .models import User, Category, Event, Daily, Priority, Status, Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, CategorySerializer, EventSerializer, DailySerializer, PrioritySerializer, StatusSerializer, TodoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class DailyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Daily.objects.all()
    serializer_class = DailySerializer

class PriorityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer