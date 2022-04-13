from .models import User, Category, Event, Daily, Priority, Status, Todo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
   
    # need the above statement if using hyperlink, can just take hyper link off
    class Meta:
        model = Category
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class DailySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Daily
        fields = '__all__'

class PrioritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'