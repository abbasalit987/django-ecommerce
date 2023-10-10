from django.shortcuts import render
from . models import Category

# Create your views here.


def store(request):
    return render(request, 'store/store.html')


def categories(request):
    return {'all_categories': Category.objects.all()}
