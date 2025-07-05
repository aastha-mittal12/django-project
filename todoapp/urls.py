from django.urls import path
from todoapp import views

urlpatterns = [
    path('homepage/', views.home_view, name='homepage'),
]
