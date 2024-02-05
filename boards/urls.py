from django.urls import path
from . import views

urlpatterns = [
    path('', views.all),
    path('first', views.first),
    path('last', views.last),
]
