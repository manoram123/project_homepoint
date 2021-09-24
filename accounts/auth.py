from django.http import HttpResponse
from django.shortcuts import redirect
from house.models import Home
from hotels.models import Hotels
from hostels.models import Hostel

# function inside function is decorator


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function


def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/admin-dashboard')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function


def access_hotel(view_function):
    def wrapper_function(request, id, *args, **kwargs):
        hotel = Hotels.objects.get(id=id)
        # print(request.user.id, hotel.user.id)
        if request.user.id != hotel.user.id:
            return HttpResponse('Unauthorized Access')
        else:
            return view_function(request, id, *args, **kwargs)
    return wrapper_function


def access_home(view_function):
    def wrapper_function(request, id, *args, **kwargs):
        home = Home.objects.get(id=id)
        # print(request.user.id, hotel.user.id)
        if request.user.id != home.user.id:
            return HttpResponse('Unauthorized Access')
        else:
            return view_function(request, id, *args, **kwargs)
    return wrapper_function


def access_hostel(view_function):
    def wrapper_function(request, id, *args, **kwargs):
        hostel = Hostel.objects.get(id=id)
        # print(request.user.id, hotel.user.id)
        if request.user.id != hostel.user.id:
            return HttpResponse('Unauthorized Access')
        else:
            return view_function(request, id, *args, **kwargs)
    return wrapper_function
