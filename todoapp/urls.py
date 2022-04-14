from django.urls import path
from . import views



urlpatterns = [
    path('', views),
    # path('<str:user_name>/')
]