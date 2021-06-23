from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from django.db.models.base import Model


from restaurant.models import Restaurant
# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length = 50, unique = True)
  email = models.EmailField(_('email address'), null = True)
  phone_no = models.CharField(max_length = 10)
  REQUIRED_FIELDS = [ 'first_name', 'last_name']
  def __str__(self):
      return "{}".format(self.email)
    

class UserRestaurants(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    added = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now=True)
    visited = models.BooleanField(default=False)
    thumbs_down = models.BooleanField(default=False)



