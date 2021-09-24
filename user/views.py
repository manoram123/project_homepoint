
from accounts.auth import access_home, access_hostel, access_hotel
from json.encoder import JSONEncoder
from django.core.checks import messages
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls.conf import path
from home.models import Home
from accounts.models import Profile
from django.shortcuts import redirect, render
from user.models import Activity, Message
from django.contrib.auth.models import User
from django.http import HttpResponse
from user.models import ChatRoom
from datetime import date
from hostels.models import Hostel
from hotels.models import Booking, Package
from hotels.models import Hotels
import PIL
from django.contrib.humanize.templatetags import humanize
import ast
from django.template.loader import render_to_string


# Create your views here.


@login_required
def user_dashboard(request):
    activity = Activity.objects.filter(user_id=request.user.id)
    context = {
        'activity': activity,
        'activate_overview': 'int-item-active'
    }
    return render(request, 'user/dashboard.html', context)


@login_required
def listings(request):
    activity = Activity.objects.filter(user_id=request.user.id)
    context = {
        'activity': activity,
        'activate_listings': 'int-item-active'
    }
    return render(request, 'user/listings.html', context)


@login_required
def bookings(request):
    activity = Activity.objects.filter(user_id=request.user.id)
    context = {
        'activity': activity,
        'activate_bookings': 'int-item-active'
    }
    return render(request, 'user/rentals.html', context)


@login_required
def profile(request):
    profile = request.user.profile
    print(profile.image)
    if request.method == 'POST':
        if "update_pic" in request.POST:
            image = request.FILES.get('profile_p')
            profile.image = image
            profile.save()
    context = {
        "profile": profile,
        'activate_profile': 'int-item-active'

    }
    return render(request, 'user/profile.html', context)


@login_required
def inbox(request):
    last_msg = ""
    room = {}
    Room2 = ChatRoom.objects.filter(person_2_id=request.user.id)
    for r in Room2:
        messages = Message.objects.filter(room_id=r.id)
        room[r] = messages
    context = {
        'room': room,
        'msg': last_msg,
        "activate_selling": "m-type-active"

    }
    return render(request, 'user/inbox.html', context)


@login_required
def inbox_buying(request):
    last_msg = ""
    room = {}
    Room1 = ChatRoom.objects.filter(person_1_id=request.user.profile.id)
    print(Room1)
    for r in Room1:
        messages = Message.objects.filter(room_id=r.id)
        room[r] = messages
    context = {
        'room': room,
        'msg': last_msg,
        "activate_buying": "m-type-active"

    }
    return render(request, 'user/inbox-buying.html', context)


@login_required
def chat(request, property_id, contact_id):
    last_msg = ''
    user_1 = request.user.id
    receiver = User.objects.get(id=contact_id)
    user_2 = User.objects.get(id=contact_id).id
    chat_room_id = (user_1+contact_id) + 1
    replied_on = Hostel.objects.get(id=property_id)

    if receiver:
        try:
            room = ChatRoom.objects.get(
                id=chat_room_id)
        except Exception as e:
            if replied_on.user.id != request.user.id:
                create_room = ChatRoom.objects.create(
                    id=chat_room_id, person_1=request.user.profile, person_2=receiver, hostel=replied_on)
    if request.method == 'POST':
        data = request.POST
        message = data['message']
        date_now = date.today().strftime("%Y-%m-%d")
        room = ChatRoom.objects.get(id=chat_room_id)
        send = Message.objects.create(
            room=room, message=message, sender=request.user, date=date_now, reply_on=replied_on)
        if send:
            return JsonResponse({'message': "Sent"})
    messages = Message.objects.filter(
        room_id=chat_room_id).order_by("timestamp")
    for msg in messages:
        last_msg = msg
    context = {
        'messages': messages,
        'property': replied_on,
        'receiver': receiver,
        'last_msg': last_msg
    }

    return render(request, 'user/message.html', context)


@login_required
def load_message(request, contact_id):
    user_1 = request.user.id
    receiver = User.objects.get(id=contact_id)
    user_2 = User.objects.get(id=contact_id).id
    chat_room_id = (user_1+contact_id) + 1
    last_msg = ""
    try:
        messages = Message.objects.filter(room=chat_room_id)
        if len(messages) > 0:
            for msgs in messages:
                last_msg = msgs
            return JsonResponse({"message": last_msg.message, "msg_id": last_msg.id, "sender": last_msg.sender_id})
        else:
            print("No messages to show")
    except:
        print("none")
    return JsonResponse({"message": "null"})


@login_required
def listing_options(request):
    return render(request, 'user/listing-options.html')


@access_hostel
def delete_hostel(request, id):
    property = Hostel.objects.get(id=id)
    property.delete()
    return redirect('/user/dashboard')


@access_home
def delete_home(request, id):
    property = Home.objects.get(id=id)
    property.delete()
    return redirect('/user/dashboard')


@access_hotel
def manage_package_hotel(request, id):
    hotel = Hotels.objects.get(id=id)
    pkg = Package.objects.filter(hotel=hotel)
    packages = {}
    for p in pkg:
        s = p.features
        if len(s) > 0:
            s = ast.literal_eval(s)
            packages[p] = s

    return render(request, 'hotels/add-package.html', {'hotel': hotel, 'packages': packages})


@access_hotel
def add_package_hotel(request, id):
    hotel = Hotels.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        type_of_stay = request.POST.get('type_of_stay')
        amentities = request.POST.getlist('amentities')
        amenities = str(amentities)
        add_package = Package.objects.create(hotel=hotel,
                                             package_title=title, price=price, features=amenities, type_of_stay=type_of_stay)
        if add_package:
            html = render_to_string('hotels/more-package-row.html', {
                'packages': add_package, "amenities": amentities
            })

    return JsonResponse({'message': "success", 'data': html})


@access_hotel
def remove_package(request, id, pkg_id):
    pkg = Package.objects.get(id=pkg_id)
    pkg.delete()
    return redirect('/user/manage-package/'+str(id))


def hotel_booking_requests(request, id):
    hotel = Hotels.objects.get(id=id)
    bookings = Booking.objects.filter(hotel=hotel)
    context = {
        'hotel': hotel,
        'bookings': bookings
    }
    return render(request, 'hotels/booking-request.html', context)
