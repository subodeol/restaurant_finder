from django.urls import include, path

from . import views

urlpatterns = [
    path('create/', views.CreateCommentView.as_view(), name='post_comment'),


]