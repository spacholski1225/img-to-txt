from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sendfile', views.sendfileinbase64, name='sendfileinbase64'),
    path('test', views.test, name='test'),
]
