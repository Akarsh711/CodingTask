from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=15, null=False, blank=False),
    address = models.CharField(max_length=100, null=False, blank=False),
    city_id = models.IntegerField(),
    zipcode = models.CharField(max_length=10, null=False, blank=False),
    locality = models.CharField(max_length=10)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    country_id = models.SmallIntegerField(),

class Offer(models.Model):
    name = models.CharField(max_length = 50, null=False, blank=False)

class FoodItems(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)
    price = models.CharField(max_length = 20, null = False, blank = False)
    offer = models.ManyToManyField(Offer)
    location = models.ManyToManyField(Location)

class Cuisine(models.Model):
    name = models.CharField(max_length = 20, null=False, blank=False)

class Rating(models.Model):
    votes = models.SmallIntegerField(default=0)
    rating_text: models.CharField(max_length=20, default="Average")
    rating_color = models.CharField(max_length=10, default="FFBA00")
    aggregate_rating: models.SmallIntegerField()
    food_item = models.ForeignKey(FoodItems, on_delete = models.CASCADE)

    def aggregateRating():
        pass

class Currency(models.Model):
    name = models.CharField(max_length=36, null=False, blank=False)

    def __str__(self):
        return self.name

class RestaurantDetail(models.Model):
    name = models.CharField(max_length=36, null=False, blank=False)
    offers = models.ForeignKey(Offer, on_delete=models.CASCADE)
    cuisines = models.ManyToManyField(Cuisine)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE)
    price_range = models.SmallIntegerField(null=False, blank=False)
    items = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    mezzo_provider = models.CharField(max_length=50)
    order_deeplink: models.URLField(max_length=200)
    has_table_booking = models.BooleanField(default=False)
    is_delivering_now = models.BooleanField(default=False)
    opentable_support = models.BooleanField(default=False)
    has_online_delivery = models.BooleanField(default=True)
    include_bogo_offers = models.BooleanField(default=False)
    average_cost_for_two = models.IntegerField(null=False, blank=False)
    switch_to_order_menu = models.BooleanField()
    is_book_form_web_view = models.BooleanField(default=True)
    book_form_web_view_url = models.URLField(max_length=200)
    is_table_reservation_supported = models.BooleanField(default=False)











# class Location(models.Model)
# class Location(models.Model)
# class Location(models.Model)
