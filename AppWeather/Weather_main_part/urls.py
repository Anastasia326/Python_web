from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/delete_city/', views.delete_city, name='delete_city'),
]
