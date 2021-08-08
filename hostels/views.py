from django.http import JsonResponse
from typing import runtime_checkable
from django.shortcuts import redirect, render
from .models import Hostel
from django.contrib import messages

# Create your views here.


def list_hostel(request):
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
        print(image1)
        print(image2)
        save = Hostel.objects.create(title=title, address=address, price=price, services=services, rules=rules, description=description,
                                     image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)
        messages.success(request, "Property Listed!")
        return redirect('/user/dashboard')

    return render(request, 'hostels/hostelform.html')
