from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('members/', views.memberList, name='members'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/details/<int:id>/', views.details, name='details'),
]