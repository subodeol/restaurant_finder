from django.shortcuts import render
from .models import Comment
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Create your views here.

class CreateCommentView(APIView):
    """
    API to create comment for a review
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant.html'

    def post(self, request):
        comment =  request.POST["comment"]
        review =  request.POST["review"]
        comment_obj = Comment.objects.create(review_id=review,comment=comment,user=request.user)
        return Response({"instance": review})
