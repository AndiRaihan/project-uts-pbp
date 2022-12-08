from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authen.models import UserProfile
from profile_page.forms import ProfileForm
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import os, traceback

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
                prevUrl = "static/" + user.image.url
                user.image = newProfpic
                os.remove(prevUrl)
        except:
            pass

        user.save()

        return HttpResponse(serializers.serialize('json', [user]), content_type="application/json")

    return HttpResponseNotFound()

@csrf_exempt
def edit_my_profile_flutter(request):
    if request.method == 'POST':
        if request.user.id == None:
            id = int(request.environ['QUERY_STRING'].split("=")[-1])
        else:
            id = request.user.id

        user = UserProfile.objects.get(user_id=id)

        alias = request.POST.get('alias')
        if alias != "": 
            user.alias = alias

        try:
            newProfpic = request.FILES['newProfpic']
            if newProfpic: 
                prevUrl = "static" + user.image.url
                
                user.image.save(newProfpic.name, newProfpic)

                if (prevUrl != "static/images/default.png"):
                    os.remove(prevUrl)
        except:
            pass

        user.save()

        return JsonResponse({"status" : "ok"})
    
    return JsonResponse({"status" : "failed"})