from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("CreateListings", views.CreateListings, name= "CreateListings"),
    path("Categories", views.Categories, name="Categories"), 
    path("listing/<str:title>", views.listing, name="listing"), 
    path("watchList/remove/<str:title>", views.remove, name="remove"), 
    path("watchList/add/<str:title>", views.add, name="add"),
    path("watchlist", views.watchList, name="watchlist"), 
    path("message/<str:title>", views.message, name="message")
]