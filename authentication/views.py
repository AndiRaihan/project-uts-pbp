from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from authen.models import UserProfile


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register(request):
    if (request.method == "POST"):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")

            new_user = User.objects.create_user(username=username, password=password)
            new_user = new_user.save()
            new_user_profile = UserProfile.objects.create(user=new_user)
            return JsonResponse({"instance": "user Dibuat"}, status=200)
        
        except:
            return JsonResponse({"instance": "gagal Dibuat"}, status=400)
        
    return JsonResponse({"instance": "gagal Dibuat"}, status=400)


@csrf_exempt
def logout(request):
	if request.user.is_authenticated or ['loggedIn']:
		if request.user.is_authenticated:
			auth_logout(request)
		return JsonResponse({"status" : "logged out"}, status=200)
	return JsonResponse({"status": "Not yet authenticated"}, status =403)
