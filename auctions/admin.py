from django.contrib import admin

from .models import Owner, Category, Listings
# Register your models here.
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Listings)