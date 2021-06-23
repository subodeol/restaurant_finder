from django.contrib.auth import forms
import users
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import UserRestaurants
from reviews.models import RestaurantReview
from .forms import SignupForm

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Create your views here.

class HomeView(APIView):
    """
    API to fetch Users Restaurants and reviews for home page
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        user_restaurants = UserRestaurants.objects.filter(user=request.user)
        user_reviews = RestaurantReview.objects.filter(given_by=request.user)
        return Response({'user_restaurants': user_restaurants,"user_reviews":user_reviews})


class SignupView(APIView):
    """
        API for User Registration
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        form = SignupForm()
        return Response({ 'form' : form })

    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        return Response({ 'form' : form })

