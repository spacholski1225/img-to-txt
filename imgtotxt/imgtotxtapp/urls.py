from django.urls import path
from . import views


urlpatterns = [
    path('sendfile', views.sendfileinbase64, name='sendfileinbase64')
]
