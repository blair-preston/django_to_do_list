from .models import User, Category, Event, Daily, Priority, Status, Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, CategorySerializer, EventSerializer, DailySerializer, PrioritySerializer, StatusSerializer, TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter




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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a category view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows an event view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class DailyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Daily.objects.all()
    serializer_class = DailySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a daily view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class PriorityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    """
    ^ Allows a priority view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    """
    ^ Allows a status view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id__name', 'user_id']
    """
    ^ Allows a todo view searching by user name bc of the foreign key relation with user_id or simply by user id
    """

