from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authen.models import UserProfile
from profile_page.forms import ProfileForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
def show_my_profile(request):
    form = ProfileForm(instance=request.user.userprofile)

    if request.method == 'POST':
        form = ProfileForm(request.POST,
                           request.FILES,
                           instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            
    context = { 'form': form }
    return render(request, 'my-profile.html', context)



    