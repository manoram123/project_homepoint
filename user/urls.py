from django.urls import path
from django.urls.resolvers import URLPattern
from user import views


urlpatterns = [
    path('dashboard/', views.user_dashboard),
    path('profile/', views.profile),
    path('listings/', views.listings),
    path('listing-options', views.listing_options),
    path('inbox/', views.inbox),
    path('chat/<int:contact_id>', views.chat)
]
