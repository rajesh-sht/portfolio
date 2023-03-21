from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio'),
    path('services', services, name='services'),
    path('newsletter', newsletter, name='newsletter'),
    path('signup', handleSignup, name='handleSignup'),
    path('login', handleLogin, name='handleLogin'),
    path('logout', handleLogout, name='handleLogout'),
    path('bloghome', bloghome, name='bloghome'),
    path('blogsingle', blogsingle, name='blogsingle'),

]
