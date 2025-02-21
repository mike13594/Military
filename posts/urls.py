from django.urls import path, include
from posts import views

urlpatterns = [
    path("", views.main),
    path("comment_add/", views.comment_add),
    path("comment_delete/<int:comment_id>/", views.comment_delete),
]