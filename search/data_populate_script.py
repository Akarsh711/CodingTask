import sys, os, csv
import django
sys.path.append('/home/bunny/Desktop/codingtask')

os.environ['DJANGO_SETTINGS_MODULE'] = 'codingtask.settings'

django.setup()
from search.models import *

# with open(path, 'r') as f:
#     reader = csv.reader(f)
#     print(dir(reader))
    # for x, row in enumerate(reader):x
    #     print(row, x)
#         print(row)



# Location
city = 
address = 
city_id = 
zipcode = 
locality = 
latitude = 
longitude = 
country_id = 

# Offer
name = 

# Cuisine
name = 

# Currency
name = 

# FoodItem
name = 
price = 
offer = MTOM
location = MTOM

# Rating
votes = 
rating_text = 
rating_color = 
aggerigate_rating = 
food_item = Foreign

# RDetail
name = 
offers = 
cuisines = 
currency = 
rating = 
price_range = 
items = 
location = 
mezzo_provider = 
order_deeplink: 
has_table_booking = 
is_delivering_now = 
opentable_support = 
has_online_delivery =
include_bogo_offers = 
average_cost_for_two = 
switch_to_order_menu = 
is_book_form_web_view = 
book_form_web_view_url = 
is_table_reservation_supported = 


