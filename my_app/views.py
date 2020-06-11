from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new_search(request):
    search = request.POST.get('search')
    return render(request, 'my_app/new_search.html')