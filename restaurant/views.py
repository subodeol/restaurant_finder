from django.shortcuts import render
from .models import Restaurant
from users.models import UserRestaurants
from reviews.models import RestaurantReview
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response




# Create your views here.

class RestaurantSearchView(APIView):
    """
        API for Restaurant View
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'

    def get(self, request):
        user_restaurants = UserRestaurants.objects.filter(user=request.user)
        return Response({'user_restaurants': user_restaurants})

    def post(self,request):
        restaurant = request.POST
        place_id = restaurant["google_place_id"]
        name = restaurant["name"]
        rating = restaurant["rating"]
        icon = restaurant["icon"]
        restaurant, created = Restaurant.objects.get_or_create(google_place_id=place_id,defaults={"name":name,"rating":rating,"icon":icon})
        user_restaurant, created = UserRestaurants.objects.get_or_create(user=request.user,restaurant=restaurant)

        user_restaurants = UserRestaurants.objects.filter(user_id=request.user)
        return Response({'user_restaurants': user_restaurants})


class AddRestaurantView(APIView):
    """
        API to add restaurant
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'

    def post(self,request):
        restaurant = request.POST
        place_id = restaurant["google_place_id"]
        name = restaurant["name"]
        rating = restaurant["rating"]
        icon = restaurant["icon"]
        restaurant, created = Restaurant.objects.get_or_create(google_place_id=place_id,defaults={"name":name,"rating":rating,"icon":icon})
        user_restaurant, created = UserRestaurants.objects.get_or_create(user=request.user,restaurant=restaurant)

        return Response({"success":True})

class RestaurantSearchView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'

    def get(self, request):
        user_restaurants = UserRestaurants.objects.filter(user=request.user)
        return Response({'user_restaurants': user_restaurants})

    def post(self,request):
        restaurant = request.POST
        place_id = restaurant["google_place_id"]
        name = restaurant["name"]
        rating = restaurant["rating"]
        icon = restaurant["icon"]
        restaurant, created = Restaurant.objects.get_or_create(google_place_id=place_id,defaults={"name":name,"rating":rating,"icon":icon})
        user_restaurant, created = UserRestaurants.objects.get_or_create(user=request.user,restaurant=restaurant)

        user_restaurants = UserRestaurants.objects.filter(user_id=request.user)
        return Response({'user_restaurants': user_restaurants})

class RestaurantView(APIView):
    """
        API to get the details of restaurant
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "restaurant.html"

    def get(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        
        reviews = RestaurantReview.objects.filter(restaurant=restaurant).prefetch_related("comments_set")
        return Response({"restaurant":restaurant,"reviews":reviews})


class RestaurantVisited(APIView):
    """
        API to add restaurant in visied list
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "restaurant.html"

    def get(self, request, id):
        user_res_obj = UserRestaurants.objects.get(id=id)
        user_res_obj.visited = True
        user_res_obj.save()
        return JsonResponse({"success":True})


class ThumbsDownView(APIView):
    """
        API for thumbs down
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "restaurant.html"

    def get(self, request,id):
        user_res_obj = UserRestaurants.objects.get(id=id)
        user_res_obj.thumbs_down = True
        user_res_obj.save()
        return JsonResponse({"success":True})
