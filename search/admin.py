from django.contrib import admin
from .models import *

class LocationAdmin(admin.ModelAdmin):
    search_fields = ['restaurant_detail__name']

class RestaurantDetailAdmin(admin.ModelAdmin):
    search_fields = ['name']

class FoodItemAdmin(admin.ModelAdmin):
    search_fields = ['restaurant_detail__name']

admin.site.register(Location, LocationAdmin)
admin.site.register(Offer)
admin.site.register(Rating)
admin.site.register(RestaurantDetail, RestaurantDetailAdmin)
admin.site.register(Cuisine)
admin.site.register(Currency)
admin.site.register(FoodItem, FoodItemAdmin)




