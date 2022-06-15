from django.urls import path

from . import views

from .views import search

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', search,name="search"),
]
