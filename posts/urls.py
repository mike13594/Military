from django.urls import path, include
from posts import views

urlpatterns = [
    path("", views.main),
]