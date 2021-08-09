from django.shortcuts import render
from hostels.models import Hostel
import json

# Create your views here.


def home(request):
    hostels = Hostel.objects.all()
    context = {
        'active_home': 'active',
        'hostels': hostels
    }
    return render(request, 'home/index.html', context)
