from django.contrib import admin
from .models import User,Comment,Bids,Listing,Wishlist
# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bids)
admin.site.register(Wishlist)