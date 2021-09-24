from accounts.auth import access_hostel
import re
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from user.models import Activity, Notifications
from django.http import JsonResponse
from typing import runtime_checkable
from django.shortcuts import redirect, render
from .models import Hostel
from django.contrib import messages
from datetime import datetime as dtm
import datetime
from hostels.models import Services, Rules, HostelBooking
from home.models import Ratings, Replies
from django.template.loader import render_to_string
# Create your views here.
date_ = datetime.date.today()


def push_noification(request, property, notifi, subject):
    notification = Notifications.objects.create(
        user=property.user, date=date_, Notification=notifi, notification_user=request.user.profile, subject=subject, datetime=dtm.now())


def list_hostel(request):
    hostels = Hostel.objects.all()
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        address = data.get('address')
        lat = data.get('lat')
        lon = data.get('lon')
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
        date_now = datetime.date.today()

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
        print(address)
        rules_s = Rules.objects.create(
            cat_friendly=cats, dog_friendly=dogs, additional_r=additional_rules
        )

        services_s = Services.objects.create(
            internet=internet, gym=gym, parking=parking, breakfast=breakfast, geyser=geyser, laundry=laundry, additional_s=additional_s)

        hostel = Hostel.objects.create(user=request.user, title=title, address=address, lat=lat, lon=lon, price=price, services=services_s, rules=rules_s, description=description, listed_date=date_now, availability=True,
                                       image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)

        if hostel:
            activity = Activity.objects.create(user=request.user,
                                               activity=hostel, activity_type="listing", property_type="Hostel", date=date_now)
            messages.success(request, "Property Listed!")
            return redirect('/user/dashboard')

    return render(request, 'hostels/hostelform.html')


@access_hostel
def edit_hostel(request, id):
    hostel = Hostel.objects.get(id=id)
    print(request.user.id)
    print(hostel.user.id)
    if request.method == 'POST':
        data = request.POST
        hostel.title = data.get('title')
        hostel.address = data.get('address')
        hostel.lat = data.get('lat')
        hostel.lon = data.get('lon')
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
            if (len(data.getlist('image2_value')) > 0 and data.getlist('image2_value')[0] == ''):
                hostel.image2 = None

        if image3 is not None:
            hostel.image3 = image3
        else:
            if (len(data.getlist('image3_value')) > 0 and data.getlist('image3_value')[0] == ''):
                hostel.image3 = None
        if image4 is not None:
            hostel.image4 = image4
        else:
            if (len(data.getlist('image4_value')) > 0 and data.getlist('image4_value')[0] == ''):
                hostel.image4 = None

        if image5 is not None:
            hostel.image5 = image5
        else:
            if (len(data.getlist('image5_value')) > 0 and data.getlist('image5_value')[0] == ''):
                hostel.image5 = None

        if image6 is not None:
            hostel.image6 = image6
        else:
            if (data.getlist('image6_value') and data.getlist('image6_value')[0] == ''):
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
    if request.user.id == hostel.user.id:
        return render(request, 'hostels/editform.html', context)
    else:
        return HttpResponse("Unauthorised Access Denied!")


def hostels(request):
    hostels = Hostel.objects.order_by('-listed_date')
    hostels = hostels[0:1]

    context = {
        'activate_hostel': 'active',
        'hostels': hostels
    }
    return render(request, 'hostels/hostels.html', context)


def load_more(request, start, end):
    hostels = Hostel.objects.order_by('-listed_date')
    hostels = hostels[start:end]
    html = render_to_string('hostels/hostel_more.html',
                            {'hostels': hostels})
    return JsonResponse({"success": "true", "data": html})


def more_comments(request, start, end, id):
    hostel = Hostel.objects.get(id=id)
    reviews = Ratings.objects.filter(hostel=hostel).order_by('-date')
    reviews = reviews[start:end]
    comments = {}
    for r in reviews:
        replies = Replies.objects.filter(comment_id=r.id)
        comments[r] = replies
    html = render_to_string('hostels/more-comments.html',
                            {'reviews': reviews, "comments": comments})
    return JsonResponse({"success": "true", "data": html})


def search(request, search):
    if request.method == "GET":
        if(len(search) > 1):
            hostels = Hostel.objects.filter(title__icontains=search)
        else:
            hostels = Hostel.objects.all()

    context = {
        'hostels': hostels
    }
    html = render_to_string('hostels/hostel_more.html', context)
    return JsonResponse({"success": "true", "data": html})


def details(request, id):
    user = request.user
    hostel = Hostel.objects.get(id=id)
    reviews = Ratings.objects.filter(hostel=hostel).order_by('-date')
    reviews = reviews[0:1]
    comments = {}
    for r in reviews:
        replies = Replies.objects.filter(comment_id=r.id)
        comments[r] = replies
    context = {
        'hostel': hostel,
        'reviews': reviews,
        'comments': comments
    }
    for com, rep in comments.items():
        print(com.comment)
        for a in rep:
            print(a.reply)
    return render(request, 'hostels/details.html', context)


def post_review_hostel(request, property_id):
    hostel = Hostel.objects.get(id=property_id)
    review = ""
    if request.method == 'POST':
        data = request.POST
        stars = data.get('rate')
        review = data.get('review')
        date_now = datetime.date.today()
        post = Ratings.objects.create(
            user=request.user, hostel=hostel, ratings=stars, comment=review, date=date_)
        post.save()
        context = {
            'post': post
        }
        html = render_to_string('reviews-comments.html', context)
        if hostel.user.id != request.user.id:
            push_noification(
                request, hostel, " posted a review:", post.comment)
    return JsonResponse({'message': review, "data": html})


# def reply_comment(request, comment_id):
#     comment = Ratings.objects.get(id=comment_id)
#     if request.method == "POST":
#         data = request.POST
#         reply = data.get('repl')
#         s = Replies.objects.create(
#             user=request.user, comment=comment, reply=reply, date=date_)
#         s.save()
#         context = {
#             'reply': s
#         }
#         html = render_to_string('reply.html', context)
#         if s:
#             if comment.user.id != request.user.id:
#                 push_noification(request, comment,
#                                  " replied on your review:", s.reply)

#     return JsonResponse({'message': 'posted', "data": html})


@login_required
def book_hostel(request, hostel_id):
    if request.method == 'POST':
        # booking_activity = Activity.objects.get(hostel_id=hostel_id
        # print(booking_activity)
        data = request.POST
        user = request.user
        hostel = Hostel.objects.get(id=hostel_id)
        duration = data.get('duration')
        adult = data.get('adult')
        child = data.get('child')
        member = adult + child
        save = HostelBooking.objects.create(
            user=user, hostel=hostel, duration=duration, adult=adult, child=child, member=member, date=date_)
        save.save()
        if save:
            activity = Activity.objects.create(user=request.user,
                                               activity=hostel, activity_type="booking", property_type="Hostel", date=date_)
            activity.save()
        if save:
            if hostel.user.id != request.user.id:
                push_noification(
                    request, hostel, " requested a booking to your hostel:", hostel.title)
    return JsonResponse({'message': "damn"})
