from hotels.models import Hotels
from django.http.response import JsonResponse
from django.shortcuts import render
from hostels.models import Hostel, Services
from house.models import Home, Services
import json
from datetime import datetime
from user.models import Notifications
from django.core import serializers
from django.contrib.humanize.templatetags import humanize


# Create your views here.


def home(request):
    hostels = Hostel.objects.order_by('-listed_date')[:6]
    homes = Home.objects.order_by('-listed_date')[:6]
    hotels = Hotels.objects.order_by('-listed_date')[:6]
    context = {
        'active_home': 'active',
        'hostels': hostels,
        'homes': homes,
        'hotels': hotels
    }
    return render(request, 'home/index.html', context)


def notifications(request):
    notifications = Notifications.objects.filter(
        user_id=request.user.id).order_by('-datetime')[:6]
    # data = serializers.serialize("json", notifications)
    # n = notifications.count()
    l = []
    for m in notifications:
        date = m.datetime
        date = humanize.naturaltime(date)
        l.append([m.notification_user.user.first_name,
                  m.Notification, date, m.subject])
    return JsonResponse({"notifications": l})
