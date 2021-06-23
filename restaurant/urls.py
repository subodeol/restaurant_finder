from django.urls import include, path
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    path('add/', login_required(views.AddRestaurantView.as_view()), name='add_restaurant'),
    path('search/', login_required(views.RestaurantSearchView.as_view()), name='restaurant_search'),
    path('<str:id>/', login_required(views.RestaurantView.as_view()),name='restaurant_view'),
    path('visited/<str:id>/', login_required(views.RestaurantVisited.as_view()), name='restaurant_visited'),
    path('thumbsdown/<str:id>/', login_required(views.ThumbsDownView.as_view()), name='restaurant_thumbsdown'),


]