from . import views
from django.urls import path
from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='memo'),
    #path('add/',views.calculation,name='calculation'),
    #path('contact/',views.contact,name='contact'),
    #path('deteals/',views.deteals,name='deteals'),
    #path('thanks/',views.thanks,name='thanks')

]
