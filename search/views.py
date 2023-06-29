from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from .models import *
from .helpers import populate, flush_data
from .helpers import add_blur, find_nearby
from django.db.models import Q


def search_by_relevance(request):
    page_number = request.GET.get("page", 1)
    name = str(request.GET.get('food_item', ''))
    location_str = str(request.GET.get('location', ''))

    if(location_str == '' or name == ''):
        context = {'search_by': 'search-by-relevance', 'name': name,
                   'error': 'Please provide the both the details'}
        return render(request, 'search.html', context=context)
    
    location = [float(i) for i in location_str.split(',')]

    latlte, longlte = add_blur(location[0], location[1], 10000)
    latgte, longgte = add_blur(location[0], location[1], -10000)

    food_item = FoodItem.objects.filter(Q(restaurant_detail__location__latitude__lte=latlte) &
                                        Q(restaurant_detail__location__longitude__lte=longlte) &
                                        Q(restaurant_detail__location__latitude__gte=latgte) &
                                        Q(restaurant_detail__location__longitude__gte=longgte) &
                                        Q(name=name)).order_by('-restaurant_detail__rating__aggregate_rating', 'price')
    paginator = Paginator(food_item, 10)
    page_obj = paginator.get_page(page_number)

    context = {'search_by': 'search-by-relevance',
               'page_obj': page_obj,
               'name': name,
               'location': location_str}

    return render(request, 'search.html', context=context)


def search_by_price(request):
    page_number = request.GET.get("page", 1)
    name = str(request.GET.get('food_item', ''))
    location_str = str(request.GET.get('location', ''))

    if(location_str == '' or name == ''):
        context = {'search_by': 'search-by-price',
                    'name': name,
                    'error': 'Please provide the both the details'}
        return render(request, 'search.html', context=context)

    location = [float(i) for i in location_str.split(',')]

    latlte, longlte = add_blur(location[0], location[1], 10000)
    latgte, longgte = add_blur(location[0], location[1], -10000)

    food_item = FoodItem.objects.filter(Q(name=name) &
                                        Q(restaurant_detail__location__latitude__lte=latlte) &
                                        Q(restaurant_detail__location__longitude__lte=longlte) &
                                        Q(restaurant_detail__location__latitude__gte=latgte) &
                                        Q(restaurant_detail__location__longitude__gte=longgte)).order_by('price')
    paginator = Paginator(food_item, 10)
    page_obj = paginator.get_page(page_number)

    context = {'search_by': 'search-by-price',
               'page_obj': page_obj,
               'name': name,
               'location': location_str}
    return render(request, 'search.html', context=context)


def search_by_rating(request):
    page_number = request.GET.get("page", 1)
    name = str(request.GET.get('food_item', ''))
    location_str = str(request.GET.get('location', ''))

    if(location_str == '' or name == ''):
        context = {'search_by': 'search-by-rating', 'name': name,
                   'error': 'Please provide the both the details'}
        return render(request, 'search.html', context=context)

    location = [float(i) for i in location_str.split(',')]

    latlte, longlte = add_blur(location[0], location[1], 10000)
    latgte, longgte = add_blur(location[0], location[1], -10000)

    food_item = FoodItem.objects.filter(Q(name=name) &
                                        Q(restaurant_detail__location__latitude__lte=latlte) &
                                        Q(restaurant_detail__location__longitude__lte=longlte) &
                                        Q(restaurant_detail__location__latitude__gte=latgte) &
                                        Q(restaurant_detail__location__longitude__gte=longgte)).order_by(
        '-restaurant_detail__rating__aggregate_rating')

    paginator = Paginator(food_item, 10)
    page_obj = paginator.get_page(page_number)

    context = {'search_by': 'search-by-rating',
               'page_obj': page_obj,
               'name': name,
               'location': location_str}
    return render(request, 'search.html', context=context)


def search_by_offer(request):
    page_number = request.GET.get("page", 1)
    name = str(request.GET.get('food_item', ''))
    location_str = str(request.GET.get('location', ''))

    if(location_str == '' or name == ''):
        context = {'search_by': 'search-by-offer', 'name': name,
                   'error': 'Please provide the both the details'}
        return render(request, 'search.html', context=context)
    location = [float(i) for i in location_str.split(',')]

    latlte, longlte = add_blur(location[0], location[1], 10000)
    latgte, longgte = add_blur(location[0], location[1], -10000)

    food_item = FoodItem.objects.filter(Q(offer__isnull=False) &
                                        Q(restaurant_detail__location__latitude__lte=latlte) &
                                        Q(restaurant_detail__location__longitude__lte=longlte) &
                                        Q(restaurant_detail__location__latitude__gte=latgte) &
                                        Q(restaurant_detail__location__longitude__gte=longgte) &
                                        Q(name=name)).order_by('-id')
    paginator = Paginator(food_item, 10)
    page_obj = paginator.get_page(page_number)

    context = {'search_by': 'search-by-offer',
               'page_obj': page_obj,
               'name': name,
               'location': location_str}
    return render(request, 'search.html', context=context)


def populate_database(request):
    populate()
    return HttpResponse('Data populated successfully')


def flush_populated_data(request):
    flush_data()
    return HttpResponse('Data flushed successfully')
