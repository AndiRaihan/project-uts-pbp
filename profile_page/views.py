from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authen.models import UserProfile
from profile_page.forms import ProfileForm
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
import os

# Create your views here.

@login_required(login_url='/login/')
def show_my_profile(request):
    form = ProfileForm(instance=request.user.userprofile)
    context = { 'form': form }
    return render(request, 'my-profile.html', context)


def get_my_profile_json(request):
    user = UserProfile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', user), content_type="application/json")

def edit_my_profile(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(user=request.user)

        alias = request.POST.get('alias')
        if alias != "": user.alias = alias

        try:
            newProfpic = request.FILES['newProfpic']
            if newProfpic: 
                beforeUrl = "static/" + user.image.url
                user.image = newProfpic
                os.remove(beforeUrl)
        except:
            pass

        user.save()

        return HttpResponse(serializers.serialize('json', [user]), content_type="application/json")

    return HttpResponseNotFound()