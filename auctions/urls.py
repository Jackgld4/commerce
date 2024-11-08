from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("CreateListings", views.CreateListings, name= "CreateListings"),
    #path("WatchList", views.WatchList, name="WatchList"),
    path("Categories", views.Categories, name="Categories"), 
    path("listing/<str:title>", views.listing, name="listing")
]