from user.models import Activity
from django.http import JsonResponse
from typing import runtime_checkable
from django.shortcuts import redirect, render
from .models import Hostel
from django.contrib import messages
from datetime import date
from hostels.models import Services, Rules
from home.models import Ratings, Replies
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
        additional_rules = data.get("additional_rules")
        description = data.get('description')
        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')
        date_now = date.today().strftime("%Y-%m-%d")

        # services
        internet = False
        gym = False
        parking = False
        breakfast = False
        geyser = False
        laundry = False

        # rules
        cats = False
        dogs = False

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

        if "Cat Allowed" in rules:
            cats = True
        if "Dog Allowed" in rules:
            dogs = True

        rules_s = Rules.objects.create(
            cat_friendly=cats, dog_friendly=dogs, additional_r=additional_rules
        )

        services_s = Services.objects.create(
            internet=internet, gym=gym, parking=parking, breakfast=breakfast, geyser=geyser, laundry=laundry, additional_s=additional_s)

        hostel = Hostel.objects.create(user=request.user, title=title, address=address, price=price, services=services_s, rules=rules_s, description=description, listed_date=date_now, availability=True,
                                       image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)

        if hostel:
            activity = Activity.objects.create(user=request.user,
                                               activity=hostel, activity_type="listing", property_type="hostel", date=date_now)
            messages.success(request, "Property Listed!")
            return redirect('/user/dashboard')

    return render(request, 'hostels/hostelform.html')


def edit_hostel(request, id):
    hostel = Hostel.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        hostel.title = data.get('title')
        hostel.address = data.get('address')
        hostel.price = data.get('price')
        services = data.getlist('services')
        rules = data.getlist('rules')
        hostel.services.additional_s = data.get('additional_features')
        hostel.rules.additional_rules = data.get("additional_rules")
        hostel.description = data.get('description')

        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')

        if image1 is not None:
            hostel.image1 = image1

        if image2 is not None:
            hostel.image2 = image2
        else:
            hostel.image2 = None

        if image3 is not None:
            hostel.image3 = image3
        else:
            hostel.image3 = None

        if image4 is not None:
            hostel.image4 = image4
        else:
            hostel.image4 = None

        if image5 is not None:
            hostel.image5 = image5
        else:
            hostel.image5 = None

        if image6 is not None:
            hostel.image6 = image6
        else:
            hostel.image6 = None

        # services
        internet = False
        gym = False
        parking = False
        breakfast = False
        geyser = False
        laundry = False

        # rules
        cats = False
        dogs = False

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

        if "Cat Allowed" in rules:
            cats = True
        if "Dog Allowed" in rules:
            dogs = True

        hostel.services.internet = internet
        hostel.services.gym = gym
        hostel.services.parking = parking
        hostel.services.breakfast = breakfast
        hostel.services.geyser = geyser
        hostel.services.laundry = laundry

        hostel.rules.cat_friendly = cats
        hostel.rules.dog_friendly = dogs
        hostel.save()
        hostel.services.save()
        hostel.rules.save()

    context = {
        'hostel': hostel
    }
    return render(request, 'hostels/editform.html', context)


def hostels(request):
    hostels = Hostel.objects.order_by('-listed_date')
    context = {
        'activate_hostel': 'active',
        'hostels': hostels
    }
    return render(request, 'hostels/hostels.html', context)


def details(request, id):
    hostel = Hostel.objects.get(id=id)
    reviews = Ratings.objects.filter(hostel=hostel).order_by('date')
    context = {
        'hostel': hostel,
        'reviews': reviews
    }
    return render(request, 'hostels/details.html', context)


def post_review_hostel(request, property_id):
    hostel = Hostel.objects.get(id=property_id)
    if request.method == 'POST':
        data = request.POST
        stars = data.get('rate')
        review = data.get('review')
        date_now = date.today().strftime("%Y-%m-%d")
        if review == "Write your review...":
            review = None
        post = Ratings.objects.create(
            user=request.user, hostel=hostel, ratings=stars, comment=review, date=date_now)
        post.save()
    return JsonResponse({'message': review})
