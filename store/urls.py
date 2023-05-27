from . import views
from django.urls import path




urlpatterns = [
    path('home/', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('search/', views.search, name='search')
]