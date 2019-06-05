from django.urls import path

from . import views

from . import feed

urlpatterns = [
    path('', views.index, name='index'),


]