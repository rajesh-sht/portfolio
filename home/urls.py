from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio'),
    # path('price', price, name='price'),
    path('services', services, name='services'),
    path('newsletter', newsletter, name='newsletter'),
    # path('element', element, name='element'),
    path('signup', handleSignup, name='handleSignup'),
    path('login', handleLogin, name='handleLogin'),
    path('logout', handleLogout, name='handleLogout'),



]
