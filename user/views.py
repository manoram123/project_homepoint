from accounts.models import Profile
from django.shortcuts import render
from user.models import Activity, Message
from django.contrib.auth.models import User
from django.http import HttpResponse
from user.models import ChatRoom
from datetime import date
# Create your views here.


def user_dashboard(request):
    activity = Activity.objects.filter(user_id=request.user.id)
    context = {
        'activity': activity,
        'activate_overview': 'int-item-active'
    }
    return render(request, 'user/dashboard.html', context)


def listings(request):

    return render(request, 'user/listings.html')


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


def inbox(request):

    return render(request, 'user/inbox.html')


def chat(request, contact_id):
    user_1 = request.user.id
    user_2 = User.objects.get(id=contact_id).id
    chat_room_id = (user_1+contact_id) + 1
    try:
        room = ChatRoom.objects.get(id=chat_room_id)
    except Exception as e:
        create_room = ChatRoom.objects.create(
            id=chat_room_id, person_1=request.user, person_2=user_2)
    if request.method == 'POST':
        data = request.POST
        message = "Hello"
        date_now = date.today().strftime("%Y-%m-%d")

        send = Message.objects.create(
            room_id=chat_room_id, message=message, sender=request.user, date=date_now)
    return HttpResponse("Done")


def listing_options(request):
    return render(request, 'user/listing-options.html')
