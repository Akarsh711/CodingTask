from django.shortcuts import render
from .models import *
def search(request):
    return render(request, 'search.html')

def search_by_relevance(request):
    pass

def search_by_price(request):
    pass

def search_by_distance(request):
    pass

def search_by_offer(request):
    pass