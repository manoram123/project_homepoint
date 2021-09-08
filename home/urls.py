from django.urls import path

from home import views

urlpatterns = [
    path('', views.home),
    path('notifications/', views.notifications)
]
