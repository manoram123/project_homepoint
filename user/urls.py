from django.urls import path
from django.urls.resolvers import URLPattern
from user import views


urlpatterns = [
    path('dashboard/', views.user_dashboard),
    path('profile/', views.profile),
    path('listings/', views.listings),
    path('bookings/', views.bookings),
    path('listing-options', views.listing_options),
    path('inbox/', views.inbox),
    path('inbox_buying/', views.inbox_buying),
    path('chat/<int:property_id>/<int:contact_id>/', views.chat),
    path('loadmessage/<int:contact_id>', views.load_message),
    path('delete-hostel/<int:id>', views.delete_hostel)
]
