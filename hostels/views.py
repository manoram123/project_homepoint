from user.models import Activity
from django.http import JsonResponse
from typing import runtime_checkable
from django.shortcuts import redirect, render
from .models import Hostel
from django.contrib import messages
from datetime import date

# Create your views here.


def list_hostel(request):
    hostels = Hostel.objects.all()
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        address = data.get('address')
        price = data.get('price')
        services = data.getlist('services')
        rules = data.getlist('rules')
        description = data.get('description')
        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')
        date_now = date.today().strftime("%d-%b-%Y")

        s_list = ["Internet", "Gym", "Bathroom",
                  "Parking", "Breakfast", "Gayser"]

        hostel = Hostel.objects.create(user=request.user, title=title, address=address, price=price, services=services, rules=rules, description=description, availability=True,
                                       image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)
        if hostel:
            activity = Activity.objects.create(user=request.user,
                                               activity=hostel, activity_type="listing", property_type="hostel", date=date_now)
            messages.success(request, "Property Listed!")
            return redirect('/user/dashboard')

    return render(request, 'hostels/hostelform.html')
