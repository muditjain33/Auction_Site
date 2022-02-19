from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    objects = None
    Category =[("Fashion","Fashion"),("Toys","Toys"),("Electronics","Electronics"),("Home","Home"),("Others","Others")]
    user = models.ForeignKey(User, related_name="listing",on_delete=models.CASCADE)
    Title=models.CharField(max_length=65)
    Description=models.TextField(max_length=255)
    Base_Price=models.IntegerField()
    Image_URL=models.URLField(max_length=900,blank=True)
    category=models.CharField(choices=Category,max_length=18,blank=True)
    noofbids=models.IntegerField(User,blank=True,default=0)
    active=models.BooleanField(User,blank=True,default=0)

    def __str__(self):
        return f"{self.Title}"

class Bids(models.Model):
    objects = None
    user = models.ForeignKey(User, related_name="bids",on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, related_name="b",on_delete=models.CASCADE)
    bids = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}:{self.bids}"

class Comment(models.Model):
    objects = None
    user = models.ForeignKey(User, related_name="comment",on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, related_name="c",on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username}:{self.comment}"

class Wishlist(models.Model):
    objects = None
    user = models.ForeignKey(User, related_name="wishlist",on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, related_name="w",on_delete=models.CASCADE)
    wishlist = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}:{self.wishlist}"