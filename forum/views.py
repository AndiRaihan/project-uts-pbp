from urllib import response
from django.shortcuts import render
from authen.models import UserProfile, Content, ContentUpvote
from forum.models import Forum, Members
from forum.forms import TaskForms, ForumForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
import json
# Create your views here.

@login_required(login_url='/login/')
def create_post(request):
    form = TaskForms(request.POST)
    response_data = {}
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            forum_id = form.cleaned_data['group']
            seller = request.user.userprofile
            content_baru = Content.objects.create(creator=seller, title=title, description=description)
            ContentUpvote.objects.create(content=content_baru)
            for pk in forum_id:
                forum = Forum.objects.get(id=pk)
                forum.contents.add(content_baru)
            return redirect('forum:json') # --> Nanti redirect ke page sebelumnya
            return HttpResponse(serializers.serialize("json", content_baru), content_type="application/json")
        else:
            messages.info(request, 'Input anda tidak valid')
    response_data['form'] = form
    response_data['forums'] = Forum.objects.all()
    return render(request, "create_post.html", response_data)

@login_required(login_url='/login/')
def create_group(request):
    form = ForumForm(request.POST)
    response_data = {}
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        creator = request.user.userprofile
        new_forum = Forum.objects.create(creator=creator, title=title, description=description)
        members = Members.objects.create(forum=new_forum)
        members.subscriptor.add(creator)
        # TODO Nanti ini ganti ke landing page utama
        return redirect('forum:group-name')
    
    response_data['form'] = form
    return render(request, "create_group.html", response_data)

@login_required(login_url='/login/')
def show_json(request):
    response_data = {}
    content = Content.objects.filter(creator=request.user.userprofile)
    response_data["user"] = json.loads(serializers.serialize("json", [request.user.userprofile]))
    response_data['data'] = json.loads(serializers.serialize("json", content))
    return JsonResponse((response_data))

@login_required(login_url='/login/')
def show_json_group(request, group_name):
    response_data = {}
    forum = Forum.objects.get(title=group_name)
    content = forum.contents.all()
    member = forum.members.subscriptor.all()
    """
    var nameMap = {};
    for (int i = 0; i < data.member.length; i++){
        nameMap[data.member[i].pk] = data.member[i].fields.alias
    }
    """
    response_data['forum'] = json.loads(serializers.serialize("json", [forum]))
    response_data['content'] = json.loads(serializers.serialize("json", content))
    return JsonResponse(response_data)

@login_required(login_url='/login/')
def get_group_name(request):
    group_name = Forum.objects.values_list('title')
    return JsonResponse({'name_list':list(group_name)})

@login_required(login_url='/login/')
def show_my_post(request):
    user_name = request.user.username
    data = Content.objects.filter(creator=request.user.userprofile)
    context = {
        'list_forum': data,
        'user_name': user_name,
    } 
    return render(request, "my-post.html", context)

@login_required(login_url='/login/')
def show_my_post_json(request):
    content = Content.objects.filter(creator=request.user.userprofile)
    return HttpResponse(serializers.serialize("json", content), content_type="application/json")

def edit_post(request, content_id):
    form = TaskForms(request.POST)
    response_data = {}
    nama = request.POST.get('name')
    description = request.POST.get('description')
    if request.method == 'POST' and nama != '' and description != '':
        id = request.POST.get('id')
        post = Content.objects.get(id=id)
        if request.POST.get('is_captured') == "true":
            if (request.POST.get('date_captured') != ''):
                # TODO Edit isi dari post-nya
                post.title = nama
                post.description = description
                post.is_captured = True
                post.date_captured = request.POST.get('date_captured')
                post.save()
                response_data['msg'] = "success"
                response_data['title'] = nama
                response_data['id'] = id
                response_data['description'] = description
                response_data['is_captured'] = True
                response_data['date_captured'] = request.POST.get('date_captured')
                response_data['date_created'] = post.date_created
                response_data['upvote_count'] = post.upvote_count
                response_data['creator_id'] = request.user.userprofile.id
                return JsonResponse(response_data)
        else:
            # TODO edit isi dari post-nya
            post.title = nama
            post.description = description
            post.is_captured = False
            post.save()
            response_data['msg'] = "success"
            response_data['title'] = nama
            response_data['id'] = id
            response_data['description'] = description
            response_data['is_captured'] = False
            response_data['date_created'] = post.date_created
            response_data['upvote_count'] = post.upvote_count
            response_data['msg'] = "success"
            response_data['creator_id'] = request.user.userprofile.id
            return JsonResponse(response_data)
    response_data['msg'] = "fail"
    return JsonResponse(response_data)