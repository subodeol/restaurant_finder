from django.db import models
from restaurant.models import Restaurant
from users.models import User

rating = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

# Create your models here.
class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    given_by = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=2,choices=rating)

