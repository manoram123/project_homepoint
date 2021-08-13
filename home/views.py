from django.shortcuts import render
from hostels.models import Hostel, Services
import json

# Create your views here.


def home(request):
    hostels = Hostel.objects.order_by('-listed_date')[:6]
    context = {
        'active_home': 'active',
        'hostels': hostels,
    }
    return render(request, 'home/index.html', context)
