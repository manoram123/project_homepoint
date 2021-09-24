from django.shortcuts import render, redirect
from hotels.models import Booking, Hotels, Package
from home.models import Ratings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from user.models import Activity, Notifications
from django.http import JsonResponse
from datetime import datetime as dtm
import datetime
from hotels.models import Services, Rules
from house.views import push_noification
from django.template.loader import render_to_string
from accounts.auth import access_hotel
import ast
date_ = datetime.date.today()


def list_hotel(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        address = data.get('address')
        lat = data.get('lat')
        lon = data.get('lon')
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
        date_now = datetime.date.today()

        # services
        breakfast = False
        internet = False
        parking = False
        # rules
        cats = False
        dogs = False
        smoking = False

        if "Internet" in services:
            internet = True

        if "Parking" in services:
            parking = True

        if "Breakfast" in services:
            breakfast = True

        if "Cat Allowed" in rules:
            cats = True
        if "Dog Allowed" in rules:
            dogs = True
        if "Smoking Allowed" in rules:
            smoking = True

        rules_s = Rules.objects.create(
            cat_friendly=cats, dog_friendly=dogs, smoking_allowed=smoking, additional_r=additional_rules
        )

        services_s = Services.objects.create(
            internet=internet, parking=parking, breakfast=breakfast, additional_s=additional_s)

        hotel = Hotels.objects.create(user=request.user, title=title, address=address, lat=lat, lon=lon, services=services_s, rules=rules_s, description=description, listed_date=date_now, availability=True,
                                      image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)

        if hotel:
            activity = Activity.objects.create(user=request.user,
                                               activity_hotel=hotel, activity_type="listing", property_type="Hotel", date=date_now)
            return redirect('/user/dashboard')

    return render(request, 'hotels/hotelform.html')


@access_hotel
def edit_hotel(request, id):
    hotel = Hotels.objects.get(id=id)
    print(hotel)
    if request.method == 'POST':
        data = request.POST
        hotel.title = data.get('title')
        hotel.address = data.get('address')
        hotel.lat = data.get('lat')
        hotel.lon = data.get('lon')
        services = data.getlist('services')
        rules = data.getlist('rules')
        hotel.services.additional_s = data.get('additional_features')
        hotel.rules.additional_rules = data.get("additional_rules")
        hotel.description = data.get('description')

        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')

        if image1 is not None:
            hotel.image1 = image1

        if image2 is not None:
            hotel.image2 = image2
        else:
            if (len(data.getlist('image2_value')) > 0 and data.getlist('image2_value')[0] == ''):
                hotel.image2 = None

        if image3 is not None:
            hotel.image3 = image3
        else:
            if (len(data.getlist('image3_value')) > 0 and data.getlist('image3_value')[0] == ''):
                hotel.image3 = None
        if image4 is not None:
            hotel.image4 = image4
        else:
            if (len(data.getlist('image4_value')) > 0 and data.getlist('image4_value')[0] == ''):
                hotel.image4 = None

        if image5 is not None:
            hotel.image5 = image5
        else:
            if (len(data.getlist('image5_value')) > 0 and data.getlist('image5_value')[0] == ''):
                hotel.image5 = None

        if image6 is not None:
            hotel.image6 = image6
        else:
            if (data.getlist('image6_value') and data.getlist('image6_value')[0] == ''):
                hotel.image6 = None

            # services
        internet = False
        parking = False
        breakfast = False
        # rules
        cats = False
        dogs = False
        smoking = False

        if "Internet" in services:
            internet = True

        if "Parking" in services:
            parking = True
        if "Breakfast" in services:
            breakfast = True
        if "Cat Allowed" in rules:
            cats = True
        if "Dog Allowed" in rules:
            dogs = True
        if "Smoking Allowed" in rules:
            smoking = True

        hotel.services.internet = internet
        hotel.services.parking = parking
        hotel.services.breakfast = breakfast

        hotel.rules.cat_friendly = cats
        hotel.rules.dog_friendly = dogs
        hotel.rules.smoking_allowed = smoking

        hotel.save()
        hotel.services.save()
        hotel.rules.save()

    context = {
        'hotel': hotel
    }
    if request.user.id == hotel.user.id:
        return render(request, 'hotels/edithotel.html', context)
    else:
        return HttpResponse("Unauthorised Access Denied!")


def details(request, id):
    user = request.user
    hotel = Hotels.objects.get(id=id)
    reviews = Ratings.objects.filter(hotel=hotel).order_by('-date')
    reviews = reviews[:6]
    # for r in reviews:
    #     last_review = r.id
    # reviews = reviews[0:5]
    pkg = Package.objects.filter(hotel=hotel)
    packages = {}
    for p in pkg:
        s = p.features
        if len(s) > 0:
            s = ast.literal_eval(s)
            packages[p] = s
    context = {
        'hotel': hotel,
        'reviews': reviews,
        'packages': packages
    }
    return render(request, 'hotels/details.html', context)


def post_review_home(request, property_id):
    hotel = Hotels.objects.get(id=property_id)
    review = ""
    html = ""
    if request.method == 'POST':
        data = request.POST
        stars = data.get('rate')
        review = data.get('review')
        date_now = datetime.date.today()
        post = Ratings.objects.create(
            user=request.user, hotel=hotel, ratings=stars, comment=review, date=date_)
        post.save()
        context = {
            'post': post
        }
        html = render_to_string('reviews-comments.html', context)
        if hotel.user.id != request.user.id:
            push_noification(
                request, hotel, " posted a review:", post.comment)
    return JsonResponse({'message': review, 'data': html})


def more_comments(request, start, end, id):
    hotel = Hotels.objects.get(id=id)
    reviews = Ratings.objects.filter(hotel=hotel).order_by('-date')
    reviews = reviews[start:end]
    comments = {}
    # for r in reviews:
    #     replies = Replies.objects.filter(comment_id=r.id)
    #     comments[r] = replies
    html = render_to_string('hotels/more-reviews.html',
                            {'reviews': reviews, "comments": comments})
    return JsonResponse({"success": "true", "data": html})


def book_hotel(request, id):
    hotel = Hotels.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        check_in_date = data.get('check-in')
        check_out_date = data.get('check-out')
        email = data.get('email')
        phone = data.get('phone')
        room_type = data.get('room_type')
        package_id = data.get('package_id')
        days_of_stay = data.get('days')
        adults = data.get('adults')
        child = data.get('child')

        package = Package.objects.get(id=package_id)

        book = Booking.objects.create(user=request.user, hotel=hotel, package=package,
                                      check_in_date=check_in_date, check_out_date=check_out_date,
                                      email=email, phone=phone, days_of_stay=days_of_stay,
                                      adults=adults, child=child, status="Pending")
        if book:
            data = "Success"
    return JsonResponse({"message": data})
