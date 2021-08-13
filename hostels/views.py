from user.models import Activity
from django.http import JsonResponse
from typing import runtime_checkable
from django.shortcuts import redirect, render
from .models import Hostel
from django.contrib import messages
from datetime import date
from hostels.models import Services
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
        additional_s = data.get('additional_features')
        description = data.get('description')
        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')
        date_now = date.today().strftime("%Y-%m-%d")
        print(date_now)
        internet = False
        gym = False
        parking = False
        breakfast = False
        geyser = False
        laundry = False

        if "Internet" in services:
            internet = True
        if "Gym" in services:
            gym = True
        if "Parking" in services:
            parking = True
        if "Breakfast" in services:
            breakfast = True
        if "Geyser" in services:
            geyser = True
        if "Laundry" in services:
            laundry = True
        services_s = Services.objects.create(
            internet=internet, gym=gym, parking=parking, breakfast=breakfast, geyser=geyser, laundry=laundry, additional_s=additional_s)

        hostel = Hostel.objects.create(user=request.user, title=title, address=address, price=price, services=services_s, description=description, listed_date=date_now, availability=True,
                                       image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)

        if hostel:
            activity = Activity.objects.create(user=request.user,
                                               activity=hostel, activity_type="listing", property_type="hostel", date=date_now)
            messages.success(request, "Property Listed!")
            return redirect('/user/dashboard')

    return render(request, 'hostels/hostelform.html')


def hostels(request):
    hostels = Hostel.objects.order_by('-listed_date')
    context = {
        'activate_hostel': 'active',
        'hostels': hostels
    }
    return render(request, 'hostels/hostels.html', context)


def details(request, id):
    hostel = Hostel.objects.get(id=id)
    context = {
        'hostel': hostel
    }
    return render(request, 'hostels/details.html', context)
