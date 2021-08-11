from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('listhostel/', views.list_hostel),
    path('details/', views.details),
    path('details/<int:id>', views.details),
    path('hostels/', views.hostels)
]
