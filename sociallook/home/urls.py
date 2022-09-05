
from django.urls import path
from . import views as home

urlpatterns = [
    path('', home.index,name='homepage'),
]
