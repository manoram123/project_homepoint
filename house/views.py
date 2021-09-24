import json
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from house.models import Home, HomeRenting, Services, Rules
from hostels.views import post_review_hostel, push_noification
from home.models import Ratings, Replies
from user.models import Activity
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from accounts.auth import access_home
import datetime
date_ = datetime.date.today()


# Create your views here.


def homes(request):
    pass


def list_home(request):
    home = Home.objects.all()
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        address = data.get('address')
        lat = data.get('lat')
        lon = data.get('lon')
        price = data.get('price')
        home_type = data.get('home_type')
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
        parking = False
        water = False
        # rules
        cats = False
        dogs = False
        smoking = False

        if "Internet" in services:
            internet = True

        if "Parking" in services:
            parking = True
        if "Water" in services:
            water = True
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
            internet=internet, parking=parking, water=water, additional_s=additional_s)

        home = Home.objects.create(user=request.user, title=title, address=address, lat=lat, lon=lon, price=price, home_type=home_type, services=services_s, rules=rules_s, description=description, listed_date=date_now, availability=True,
                                   image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)

        if home:
            activity = Activity.objects.create(user=request.user,
                                               activity_home=home, activity_type="listing", property_type="Home", date=date_now)
            return redirect('/user/dashboard')

    return render(request, 'house/homeform.html')


@access_home
def edit_home(request, id):
    home = Home.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        home.title = data.get('title')
        home.address = data.get('address')
        home.lat = data.get('lat')
        home.lon = data.get('lon')
        home.price = data.get('price')
        services = data.getlist('services')
        rules = data.getlist('rules')
        home.services.additional_s = data.get('additional_features')
        home.rules.additional_rules = data.get("additional_rules")
        home.description = data.get('description')

        image1 = request.FILES.get('image_1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')

        if image1 is not None:
            home.image1 = image1

        if image2 is not None:
            home.image2 = image2
        else:
            if (len(data.getlist('image2_value')) > 0 and data.getlist('image2_value')[0] == ''):
                home.image2 = None

        if image3 is not None:
            home.image3 = image3
        else:
            if (len(data.getlist('image3_value')) > 0 and data.getlist('image3_value')[0] == ''):
                home.image3 = None
        if image4 is not None:
            home.image4 = image4
        else:
            if (len(data.getlist('image4_value')) > 0 and data.getlist('image4_value')[0] == ''):
                home.image4 = None

        if image5 is not None:
            home.image5 = image5
        else:
            if (len(data.getlist('image5_value')) > 0 and data.getlist('image5_value')[0] == ''):
                home.image5 = None

        if image6 is not None:
            home.image6 = image6
        else:
            if (data.getlist('image6_value') and data.getlist('image6_value')[0] == ''):
                home.image6 = None

         # services
        internet = False
        parking = False
        water = False
        # rules
        cats = False
        dogs = False
        smoking = False

        if "Internet" in services:
            internet = True

        if "Parking" in services:
            parking = True
        if "Water" in services:
            water = True
        if "Cat Allowed" in rules:
            cats = True
        if "Dog Allowed" in rules:
            dogs = True
        if "Smoking Allowed" in rules:
            smoking = True

        home.services.internet = internet
        home.services.parking = parking
        home.services.water = water

        home.rules.cat_friendly = cats
        home.rules.dog_friendly = dogs
        home.rules.smoking_allowed = smoking

        home.save()
        home.services.save()
        home.rules.save()

    context = {
        'home': home
    }
    if request.user.id == home.user.id:
        return render(request, 'house/edithome.html', context)
    else:
        return HttpResponse("Unauthorised Access Denied!")


def rooms(request, type):
    home = Home.objects.filter(
        home_type=type).order_by('-listed_date')
    home = home[0:2]

    context = {
        'activate_rooms': 'active',
        'home': home
    }
    return render(request, 'house/rooms.html', context)


def flats(request, type):
    home = Home.objects.filter(
        home_type=type).order_by('-listed_date')
    home = home[0:2]

    context = {
        'activate_flats': 'active',
        'home': home
    }
    return render(request, 'house/rooms.html', context)


def load_more(request, start, end, type):
    home = Home.objects.order_by('-listed_date')
    home = home[start:end]
    html = render_to_string('house/more_home.html',
                            {'home': home})
    return JsonResponse({"success": "true", "data": html})


def details(request, id):
    last_review = 0
    user = request.user
    home = Home.objects.get(id=id)
    reviews = Ratings.objects.filter(home=home).order_by('-date')
    reviews = reviews[:6]
    for r in reviews:
        last_review = r.id
    # reviews = reviews[0:5]
    comments = {}
    for r in reviews:
        replies = Replies.objects.filter(comment_id=r.id)
        comments[r] = replies
    context = {
        'home': home,
        'reviews': reviews,
        'comments': comments,
        'last': last_review
    }
    return render(request, 'house/details.html', context)


def post_review_home(request, property_id):
    home = Home.objects.get(id=property_id)
    review = ""
    if request.method == 'POST':
        data = request.POST
        stars = data.get('rate')
        review = data.get('review')
        date_now = datetime.date.today()
        post = Ratings.objects.create(
            user=request.user, home=home, ratings=stars, comment=review, date=date_)
        post.save()
        context = {
            'post': post
        }
        html = render_to_string('reviews-comments.html', context)
        if home.user.id != request.user.id:
            push_noification(
                request, home, " posted a review:", post.comment)
    return JsonResponse({'message': review, 'data': html})


def more_comments(request, start, end, id):
    home = Home.objects.get(id=id)
    reviews = Ratings.objects.filter(home=home).order_by('-date')
    reviews = reviews[start:end]
    comments = {}
    # for r in reviews:
    #     replies = Replies.objects.filter(comment_id=r.id)
    #     comments[r] = replies
    html = render_to_string('house/more-reviews.html',
                            {'reviews': reviews, "comments": comments})
    return JsonResponse({"success": "true", "data": html})


def load_reviews(request, id):
    post = Ratings.objects.all().reverse()[0]
    context = {
        'post': post
    }
    html = render_to_string('reviews-comments.html', context)
    return JsonResponse({'id': post.id, 'data': html})


def search(request, search):
    if request.method == "GET":
        if(len(search) > 1):
            home = Home.objects.filter(
                title__icontains=search)
        else:
            home = Home.objects.all()
            home = home[:2]

    context = {
        'home': home
    }
    html = render_to_string('house/more_home.html', context)
    return JsonResponse({"success": "true", "data": html})

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

#     return JsonResponse({'message': 'posted', 'data': html})


@login_required
def book_rent_home(request, id):
    if request.method == 'POST':
        # booking_activity = Activity.objects.get(hostel_id=hostel_id
        # print(booking_activity)
        data = request.POST
        user = request.user
        home = Home.objects.get(id=id)
        duration = data.get('duration')
        adult = data.get('adult')
        child = data.get('child')
        member = int(adult) + int(child)

        if int(child) > 2:
            return JsonResponse({"message": "expChild"})
        elif int(adult) > 3:
            return JsonResponse({"message": "expAdult"})
        elif int(member) > 5:
            return JsonResponse({"message": "expMember"})

        else:
            save = HomeRenting.objects.create(
                user=user, home=home, duration=duration, adult=adult, child=child, member=member, date=date_)
            save.save()
            if save:
                activity = Activity.objects.create(user=request.user,
                                                   activity_home=home, activity_type="rent", property_type="Home", date=date_)
                activity.save()
                return JsonResponse({'message': "success"})
            if save:
                if home.user.id != request.user.id:
                    push_noification(
                        request, home, " requested a booking to your hostel:", home.title)
    return JsonResponse({'message': "damn"})
