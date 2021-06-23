from django.db import models
from reviews.models import RestaurantReview
from users.models import User
# Create your models here.

class Comment(models.Model):
    review = models.ForeignKey(RestaurantReview,on_delete=models.CASCADE,related_name ="comments_set")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
