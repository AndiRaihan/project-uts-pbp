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
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware
import datetime
# Create your views here.


@login_required(login_url='/login/')
def create_post(request):
    form = TaskForms(request.POST)
    response_data = {}
    if request.method == 'POST':
        print(request.POST.get("group"))
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            forum_id = form.cleaned_data['group']
            print(forum_id)
            seller = request.user.userprofile
            content_baru = Content.objects.create(
                creator=seller, title=title, description=description)
            ContentUpvote.objects.create(content=content_baru)
            for pk in forum_id:
                forum = Forum.objects.get(id=pk)
                forum.contents.add(content_baru)
            return redirect('timeline:landing')

        else:
            messages.info(request, 'Input anda tidak valid')
    response_data['form'] = form
    response_data['forums'] = Forum.objects.all()
    return render(request, "create_post.html", response_data)


@csrf_exempt
@login_required(login_url='/login/')
def create_post_flutter(request):
    form = TaskForms(request.POST)
    response_data = {}
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        group = request.POST.get("group")
        list_of_char = ["[", "]", ","]
        # Create a mapping table to map the characters
        # to be deleted with empty string
        translation_table = str.maketrans('', '', ''.join(list_of_char))
        group = group.translate(translation_table)
        group = group.split(" ")
        forum_id = [int(i) for i in group]

        seller = request.user.userprofile
        content_baru = Content.objects.create(
            creator=seller, title=title, description=description)
        ContentUpvote.objects.create(content=content_baru)
        for pk in forum_id:
            forum = Forum.objects.get(id=pk)
            forum.contents.add(content_baru)
        return JsonResponse({"status": "oke"})
    response_data['form'] = form
    response_data['forums'] = Forum.objects.all()
    print("Masuk 3")
    return JsonResponse({"status": "gagal"})


@login_required(login_url='/login/')
def create_group(request):
    form = ForumForm(request.POST)
    response_data = {}
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        creator = request.user.userprofile
        new_forum = Forum.objects.create(
            creator=creator, title=title, description=description)
        members = Members.objects.create(forum=new_forum)
        members.subscriptor.add(creator)
        # TODO Nanti ini ganti ke landing page utama
        return redirect('timeline:landing')

    response_data['form'] = form
    return render(request, "create_group.html", response_data)


@csrf_exempt
@login_required(login_url='/login/')
def create_group_flutter(request):
    form = ForumForm(request.POST)
    response_data = {}
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        creator = request.user.userprofile
        new_forum = Forum.objects.create(
            creator=creator, title=title, description=description)
        members = Members.objects.create(forum=new_forum)
        members.subscriptor.add(creator)
        # TODO Nanti ini ganti ke landing page utama
        return JsonResponse({"status": "oke"})

    return JsonResponse({"status": "gagal"})


@login_required(login_url='/login/')
def show_json(request):
    response_data = {}
    content = Content.objects.filter(creator=request.user.userprofile)
    response_data["user"] = json.loads(
        serializers.serialize("json", [request.user.userprofile]))
    response_data['data'] = json.loads(serializers.serialize("json", content))
    return JsonResponse((response_data))

# @login_required(login_url='/login/')


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
    response_data['content'] = json.loads(
        serializers.serialize("json", content))
    return JsonResponse(response_data)


@login_required(login_url='/login/')
def get_group_name(request):
    group_name = Forum.objects.values_list('title')
    return JsonResponse({'name_list': list(group_name)})


@login_required(login_url='/login/')
def show_my_post(request):
    user_name = request.user.username
    data = Content.objects.filter(creator=request.user.userprofile)
    context = {
        'list_forum': data,
        'user_name': user_name,
    }
    return render(request, "my-post.html", context)

# TODO Jadiin login required


@login_required(login_url='/login/')
def show_my_post_json(request):
    content = Content.objects.filter(creator=request.user.userprofile)
    return HttpResponse(serializers.serialize("json", content), content_type="application/json")


@csrf_exempt
@login_required(login_url='/login/')
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
                date = request.POST.get('date_captured')
                post.date_captured = date
                post.save()
                response_data['msg'] = "success"
                response_data['title'] = nama
                response_data['id'] = id
                response_data['description'] = description
                response_data['is_captured'] = True
                response_data['date_captured'] = date
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

@csrf_exempt
@login_required(login_url='/login/')
def edit_post_flutter(request, content_id):
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
                date = request.POST.get('date_captured')
                try:
                    date_fix = datetime.datetime.strptime(
                        date, "%Y-%m-%dT%H:%M:%SZ")
                except:
                    date_fix = datetime.datetime.strptime(
                        date, "%Y-%m-%d %H:%M:%S.%f")
                date_fix = make_aware(date_fix)
                post.date_captured = date_fix
                post.save()
                response_data['msg'] = "success"
                response_data['title'] = nama
                response_data['id'] = id
                response_data['description'] = description
                response_data['is_captured'] = True
                response_data['date_captured'] = date
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


def delete_post(request, content_id):
    content = Content.objects.get(id=content_id)
    content.delete()
    return JsonResponse({'msg': 'Success'})
