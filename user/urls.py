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
    path('delete-hostel/<int:id>', views.delete_hostel),
    path('delete-home/<int:id>', views.delete_home),
    path('manage-package/<int:id>', views.manage_package_hotel),
    path('add-package/<int:id>', views.add_package_hotel),
    path('remove-package/<int:id>/<int:pkg_id>', views.remove_package),
    path('hotel-booking-requests/<int:id>', views.hotel_booking_requests)

]
