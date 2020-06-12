import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new_search(request):
    search = request.POST.get('search')
    return render(request, 'my_app/new_search.html')