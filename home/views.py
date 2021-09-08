from django.http.response import JsonResponse
from django.shortcuts import render
from hostels.models import Hostel, Services
import json
from user.models import Notifications
from django.core import serializers


# Create your views here.


def home(request):
    hostels = Hostel.objects.order_by('-listed_date')[:6]
    context = {
        'active_home': 'active',
        'hostels': hostels,
    }
    return render(request, 'home/index.html', context)


def notifications(request):
    notifications = Notifications.objects.filter(
        user_id=request.user.id)
    data = serializers.serialize("json", notifications)
    n = notifications.count()
    l = []
    for m in notifications:
        image = m.user.profile.image
        img = str(image)
        img.replace("static/users/", "")
        print(img)
        l.append([m.Notification, m.date, str(image)])
    return JsonResponse({"notifications": l})
