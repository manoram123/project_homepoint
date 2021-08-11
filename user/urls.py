from django.urls import path
from django.urls.resolvers import URLPattern
from user import views


urlpatterns = [
    path('dashboard/', views.user_dashboard),
    path('profile/', views.profile),
    path('listing-options', views.listing_options)
]
