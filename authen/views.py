import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from authen.models import UserProfile
import json


# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == "POST" and is_ajax:
        form = UserCreationForm(request.POST)
        data = {}
        if form.is_valid():
            user = form.save()
            data['success'] = True
            user_profile = UserProfile.objects.create(user=user)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data['error'] = form.errors
            data['success'] = False
            return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        context = {'form':form}
    return render(request, 'register.html', context)

def is_ajax(request):
  return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_profile_pk'] = UserProfile.objects.get(user=user).pk
            request.session.set_expiry(1800)
            return redirect('timeline:landing') # Nanti redirect ke timeline
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authen:login')