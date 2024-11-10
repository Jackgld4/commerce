from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Listings, Category, Owner


def index(request):
    activeListings = Listings.objects.filter(active=True).order_by('title')
    return render(request, "auctions/index.html", {
        "activeListings": activeListings
    })

def listing(request, title): 
    listingID=Listings.objects.get(title=title)
    listingInWatchlist= request.user in listingID.watchList.all()
    return render(request, "auctions/listing.html", {
        "listing":listingID, 
        "listingInWatchList": listingInWatchlist
        })

def remove(request, title): 
    listingID=Listings.objects.get(title=title)
    user= request.user
    listingID.watchList.remove(user)
    return HttpResponseRedirect(reverse("listing", args=(title, )))

def add(request, title): 
    listingID=Listings.objects.get(title=title)
    user= request.user
    listingID.watchList.add(user)
    return HttpResponseRedirect(reverse("listing", args=(title, )))

def watchList(request):
    user= request.user
    listings= user.watchList.all()
    return render(request, "auctions/watchlist.html", { 
             "listing": listings
            })

def CreateListings(request):
    if request.method== "GET":
        categoryList= Category.objects.all()
        return render(request, "auctions/CreateListings.html", {
            "categories": categoryList
        })
    else: 
        title=request.POST.get('title')
        imageUrl=request.POST.get('imageUrl')
        description=request.POST.get('description')
        price=request.POST.get('price')
 #       owner=request.user
        #active=request.POST.get('active')
        category=request.POST.get('category')
        #Get List of Categories and Owners to save to 
        category_obj = Category.objects.get(CategoryName=category)
 #      Owner_obj=Owner.objects.get(OwnerName=owner)
        NewListing= Listings(
            title=title, 
            imageUrl=imageUrl,
            description=description, 
            price=price,
 #           owner=Owner_obj, 
           # active=active,
            category=category_obj
        )
        NewListing.save()
        return HttpResponseRedirect(reverse("index"))

# def WatchList(request):
#     {% if User selects a Watchlist item }
#     return render(request, "auctions/index.html", {
#        "active_listings": active_listings
#    })

def Categories(request):
    categories = Category.objects.all()
    selectedCategory = request.GET.get('category')
    if selectedCategory:
        selectedListings = Listings.objects.filter(category__CategoryName=selectedCategory).order_by('title')
    else:
        selectedListings = Listings.objects.all().order_by('title')
    return render(request, 'auctions/Categories.html', {
        'categories': categories,
        'listings': selectedListings,
        'selectedCategory': selectedCategory
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
