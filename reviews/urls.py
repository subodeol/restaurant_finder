from django.urls import include, path

from . import views

urlpatterns = [
    path('create/', views.ReviewView.as_view(), name='create_review'),
]