from django.http import HttpResponse
from django.shortcuts import redirect

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