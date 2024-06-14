from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('name/<str:name>/', views.detail, name = 'detail'),
    path('/', views.add_bunk, name = 'add_bunk'),

]