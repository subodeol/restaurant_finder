from django.shortcuts import render
from django.http import JsonResponse
from .models import RestaurantReview
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


# Create your views here.


class ReviewView(APIView):
    """
    API to create review for a restaurant.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant.html'

    def post(self, request):
        rate =  request.POST["rate"]
        review =  request.POST["review"]
        restaurant = request.POST["restaurant"]
        res_review, created = RestaurantReview.objects.get_or_create(given_by=request.user,restaurant_id=restaurant,
        defaults={"rating":rate,"review":review})
        return Response({"instance": review})



