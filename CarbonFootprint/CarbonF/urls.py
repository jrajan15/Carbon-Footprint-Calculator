from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('calculate', views.calculate, name="Calculate"),
    path('about', views.about, name="About"),
    path('',views.getResponse)
]
