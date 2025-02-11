from django.urls import path
from . import views

urlpatterns = [
    path('', views.memberList, name='members'),
    path('add/', views.add_member, name='add_member'),
    path('details/<int:id>/', views.details, name='details'),
]