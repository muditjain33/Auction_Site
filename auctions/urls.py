from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("category", views.category, name="category"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("<int:itemid>", views.item, name="item"),
    path("activetoun/<int:itemid>", views.activetoun, name="activetoun"),
    path("category/<str:name>", views.SpecificCategory, name="SpecificCategory")
]
