from accounts.models import Profile
from django.shortcuts import render
from user.models import Activity
from django.contrib.auth.models import User

# Create your views here.


def user_dashboard(request):
    activity = Activity.objects.filter(user_id=request.user.id)
    context = {
        'activity': activity
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
        "profile": profile

    }
    return render(request, 'user/profile.html', context)
