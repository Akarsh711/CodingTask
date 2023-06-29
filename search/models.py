from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=36, null=False, blank=False)
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    votes = models.SmallIntegerField(default=0)
    rating_text = models.CharField(max_length=20, default="Average")
    rating_color = models.CharField(max_length=10, default="FFBA00")
    aggregate_rating = models.CharField(max_length=11)

    def __str__(self):
        return str(self.id) + ":" + str(self.votes)
    
class RestaurantDetail(models.Model):
    name = models.CharField(max_length=36, null=False, blank=False)
    cuisines = models.ManyToManyField(Cuisine)
    currency = models.ManyToManyField(Currency) # many to one field
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE)
    price_range = models.SmallIntegerField(null=False, blank=False)
    mezzo_provider = models.CharField(max_length=50)
    order_deeplink = models.URLField(max_length=200, null=True, blank=True)
    has_table_booking = models.BooleanField(default=False)
    is_delivering_now = models.BooleanField(default=False)
    opentable_support = models.BooleanField(default=False)
    has_online_delivery = models.BooleanField(default=True)
    include_bogo_offers = models.BooleanField(default=False)
    average_cost_for_two = models.IntegerField(null=False, blank=False)
    switch_to_order_menu = models.BooleanField()
    is_book_form_web_view = models.BooleanField(default=True)
    book_form_web_view_url = models.URLField(max_length=200, null=True, blank=True)
    is_table_reservation_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=15, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    city_id = models.IntegerField()
    zipcode = models.CharField(max_length=10, null=False, blank=False)
    locality = models.CharField(max_length=10)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    country_id = models.SmallIntegerField()
    restaurant_detail = models.ForeignKey(RestaurantDetail, on_delete=models.CASCADE) # many to one field

    def __str__(self):
        return self.address


class Offer(models.Model):
    name = models.TextField()

    restaurant_detail = models.ForeignKey(RestaurantDetail, on_delete=models.CASCADE, null=True, blank=True)  # many to one field
    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.CharField(max_length=20, null=False, blank=False)
    offer = models.ManyToManyField(Offer)
    restaurant_detail = models.ForeignKey(RestaurantDetail, on_delete=models.CASCADE) # many to one field

    def __str__(self):
        return self.name

