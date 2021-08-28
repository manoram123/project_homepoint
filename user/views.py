from django.core.checks import messages
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from django.shortcuts import render
from user.models import Activity, Message
from django.contrib.auth.models import User
from django.http import HttpResponse
from user.models import ChatRoom
from datetime import date
from hostels.models import Hostel
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

    return render(request, 'user/listings.html')


@login_required
def profile(request):
    profile = request.user.profile
    print(profile.image)
    if request.method == 'POST':
        if "update_pic" in request.POST:
            image = request.FILES.get('profile_p')
            print(image)
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
    Room2 = ChatRoom.objects.filter(person_2=request.user.id)
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
    Room1 = ChatRoom.objects.filter(person_1=request.user.id)
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
            create_room = ChatRoom.objects.create(
                id=chat_room_id, person_1=request.user.profile, person_2=receiver)
    if request.method == 'POST':
        data = request.POST
        message = data['message']
        date_now = date.today().strftime("%Y-%m-%d")
        room = ChatRoom.objects.get(id=chat_room_id)
        send = Message.objects.create(
            room=room, message=message, sender=request.user, date=date_now, reply_on=replied_on)
        if send:
            return JsonResponse({'message': "Sent"})
    messages = Message.objects.filter(room_id=chat_room_id)
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


@login_required
def rate(request, property_id):
    pass
