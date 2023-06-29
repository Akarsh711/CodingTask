import math
import os, json
from .models import *
import pandas as pd

path = (os.path.abspath(os.path.join('.', 'restaurants_small.csv')))
df = pd.read_csv(path)

# ------------------METHOD FOR LOCATION HELP-------------------------

def add_blur(lat, long, meters):
    blur_factor = meters * 0.000006279
    new_lat = lat + blur_factor
    new_long = long + blur_factor / math.cos(lat * 0.018)
    return new_lat, new_long

def find_nearby(location_str):
    location = location_str
    if location == None:
        return None
    
    location = [float(i) for i in location.split(',')]

    latlte, longlte = add_blur(location[0], location[1], 10000)
    latgte, longgte = add_blur(location[0], location[1], -10000)

    location_data = Location.objects.filter(latitude__lte = latlte, longitude__lte = longlte).filter(latitude__gte = latgte, longitude__gte = longgte)
    print(location_data)
    return location_data

# ------------------METHODS FOR DATA POPULATION-----------------------

def populate():
    for i in range(df.shape[0] - 1):
        iterate_and_populate(i)


def flush_data():
    Cuisine.objects.all().delete()
    Rating.objects.all().delete()
    RestaurantDetail.objects.all().delete()
    Location.objects.all().delete()
    Offer.objects.all().delete()
    FoodItem.objects.all().delete()
    Currency.objects.all().delete()


def iterate_and_populate(i):
    print('updating row ... ',i)
    food_items_list = df.loc[:,"items"]
    food_items = json.loads(food_items_list[i])
    full_detail = df.full_details
    try:
        detail = json.loads(full_detail[i])
    except:
        return


    # CHECKS
    if 'is_book_form_web_view' not in detail:
        detail['is_book_form_web_view'] = None
    
    if 'mezzo_provider' not in detail:
        detail['mezzo_provider'] = None

    if 'order_deeplink' not in detail:
        detail['order_deeplink'] = None
    
    if 'has_table_booking' not in detail:
        detail['has_table_booking'] = None

    if 'is_delivering_now' not in detail:
        detail['is_delivering_now'] = None

    if 'opentable_support' not in detail:
        detail['opentable_support'] = None


    if 'has_online_delivery' not in detail:
        detail['has_online_delivery'] = None

    if 'include_bogo_offers' not in detail:
        detail['include_bogo_offers'] = None

    if 'average_cost_for_two' not in detail:
        detail['average_cost_for_two'] = None

    if 'switch_to_order_menu' not in detail:
        detail['switch_to_order_menu'] = None

    
    if 'is_book_form_web_view' not in detail:
        detail['is_book_form_web_view'] = None
    
    
    if 'book_form_web_view_url' not in detail:
        detail['book_form_web_view_url'] = None
    
    if 'is_table_reservation_supported' not in detail:
        detail['is_table_reservation_supported'] = None



    # CUOSINE MODEL
    cuisines_list = []
    for name in detail['cuisines'].split(','):
        cuisine, created = Cuisine.objects.get_or_create(name =  name)
        cuisines_list.append(cuisine)

     # CURRENCY MODEL
    currencies_list = []
    for name in detail['currency'].split(','):
        currency, created = Currency.objects.get_or_create(name =  name)
        currencies_list.append(currency)

    # RATING MODEL
    rating = Rating(
        votes = detail['user_rating']['votes'],
        rating_text = detail['user_rating']['rating_text'],
        rating_color = detail['user_rating']['rating_color'],
        aggregate_rating = detail['user_rating']['aggregate_rating'],
    )
    rating.save()


    # RESTAURANTDETAIL MODEL
    restaurant_detail = RestaurantDetail(
    name = detail['name'],
    rating = rating,
    price_range = detail['price_range'],
    mezzo_provider = detail['mezzo_provider'],
    order_deeplink = detail['order_deeplink'],
    has_table_booking = detail['has_table_booking'],
    is_delivering_now = detail['is_delivering_now'],
    opentable_support = detail['opentable_support'],
    has_online_delivery = detail['has_online_delivery'],
    include_bogo_offers = detail['include_bogo_offers'],
    average_cost_for_two = detail['average_cost_for_two'],
    switch_to_order_menu = detail['switch_to_order_menu'],
    is_book_form_web_view = detail['is_book_form_web_view'],
    book_form_web_view_url = detail['book_form_web_view_url'],
    is_table_reservation_supported = detail['is_table_reservation_supported']
    )
    restaurant_detail.save()
    restaurant_detail.cuisines.add(*cuisines_list)
    restaurant_detail.currency.add(*currencies_list)


    # LOCATION MODEL
    location = Location(
        city = detail['location']['city'],
        address = detail['location']['address'],
        city_id = detail['location']['city_id'],
        zipcode = detail['location']['zipcode'],
        locality = detail['location']['locality'],
        latitude = detail['location']['latitude'],
        longitude = detail['location']['longitude'],
        country_id = detail['location']['country_id'],
        restaurant_detail = restaurant_detail
    )
    location.save()


    # OFFER MODEL
    offers_list = []
    print('offer_list before', offers_list)
    for name in detail['offers']:
        offer = Offer(name = str(name), restaurant_detail = restaurant_detail)
        offer.save()

        offers_list.append(offer)
    print('offer_list after', offers_list)
    

    # FOODITEM MODEL
    food_items_list = []
    for key in food_items:
        food_item = FoodItem(
        name = key,
        price = food_items[key],
        restaurant_detail = restaurant_detail
        )
        food_item.save()
        for offer in offers_list:
            food_item.offer.add(offer)

        food_items_list.append(food_item)
