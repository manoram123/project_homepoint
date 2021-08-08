from accounts.models import Profile
from django.shortcuts import render

# Create your views here.


def user_dashboard(request):

    return render(request, 'user/dashboard.html')


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
