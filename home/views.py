from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    views = {}
    # ORM -> Object Relational Mapping
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request, 'index.html', views)


def about(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    return render(request, 'about.html', views)


def contact(request):
    views = {}
    views['informations'] = Information.objects.all()
    return render(request, 'contact.html', views)


def portfolio(request):

    return render(request, 'portfolio.html')


def price(request):

    return render(request, 'price.html')


def services(request):
    views = {}
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request, 'services.html', views)
