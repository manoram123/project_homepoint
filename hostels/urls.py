from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('listhostel/', views.list_hostel)
]
