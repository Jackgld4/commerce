from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Owner(models.Model):
    OwnerName= models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.OwnerName}"
    
class Category(models.Model):
    CategoryName= models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.CategoryName}"

# class Bid(models.Model):
#    bid = models.FloatField(default=0)
#    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="userBid", default=1)

#     def __str__(self):
#         return f"{self.bid}" 

class Listings(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    imageUrl = models.URLField()
    description = models.TextField(max_length=500)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ownerListing", default=1)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= "category")
    watchList = models.ManyToManyField(User, blank= True, related_name="watchList")

    def __str__(self):
        return f"{self.title}"
    
         

    