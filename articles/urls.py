from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('portal/', price, name='portal'),
    path('about/', about, name='about'),
    path('team/', xodim, name='team'),
    path('qaror/', qaror, name='qaror'),
    path('xujjat/', document, name='document'),
    path('tuzilma/', tuzilma, name='tuzilma'),
    path('farmon/', farmon, name='farmon'),
    path('service/', service, name='service'),
    path('price/<int:pk>/', price_plan, name='price_plan'),
    path('contact/', contact, name='contact'),
    path('yangiliklar/', yangilik, name='news'),
    path('batafsil/<int:pk>/', detailview, name='detail'),
]
