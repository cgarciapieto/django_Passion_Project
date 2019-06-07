from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('createpost/', views.createpost, name='createpost'),
    path('test/', views.post_list, name='post_list'),
    path('', views.index, name='index'),


]