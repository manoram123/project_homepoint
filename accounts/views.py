from django.contrib import messages, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from accounts.models import Profile


# Create your views here.
from accounts.auth import unauthenticated_user


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        data = request.POST
        useri = data['username']
        password = data['password']
        try:
            username = User.objects.get(username=useri)
            print(username)
        except:
            return JsonResponse({"message": ['error', "User does not exists!"]})
        if username is not None:
            user = auth.authenticate(
                request, username=username, password=password)
            if user is not None:
                login(request, user)
                usr = User.objects.get(username=useri)
                return JsonResponse({"message": ["success", "Logged in!"]})
            else:
                return JsonResponse({"message": ['error', "Incorrect password!"]})
    return render(request, 'accounts/login.html')


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        email = data['email']
        phone = data['phone']
        username = data['username']
        passw = data['password']
        cpassw = data['confirm_password']
        if passw != cpassw:
            return JsonResponse({"message": ['error', "Password did not match!"]})

        elif len(username) < 6:
            return JsonResponse({"message": ['error', "Username must contain at least 6 characters!"]})
        else:
            if User.objects.filter(username=username).exists():
                return JsonResponse({"message": ['error', "Username is already taken!"]})
            else:
                try:
                    user = User.objects.create(
                        username=username, first_name=name, email=email)
                    user.set_password(passw)
                    user.save()
                    if user:
                        reg_success = messages.info(
                            request, 'Successfully registered!')
                        print(reg_success)
                        profile = Profile.objects.create(
                            user=user, phone=phone, active_status=True, verified=False)
                        return JsonResponse({"message": ['success', "Successfully registered! Please Wait..."]})

                except Exception as e:
                    print(e)
    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out!")
    return redirect("/")
