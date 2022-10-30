from django.shortcuts import redirect, render
from authen.models import Content
from forum.models import Forum
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from timeline.models import Comment
from timeline.forms import CommentForms
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_timeline(request,group_name):
    forum = Forum.objects.get(title=group_name)
    data = forum.contents.all()
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        user_name = "Anonymous"
    
    
    context = {
        'list_forum': data,
        'user_name': user_name,
    } 
    return render(request, "timeline.html", context)


def show_group(request):
    data = Forum.objects.all()
    context={
        'list_group':data
    }
    return render(request,'home.html',context)

# butuh @
@login_required(login_url='/login/')
def comment(request,group_name,content_id):
    content = Content.objects.get(id=content_id) 
    form = CommentForms(request.POST)
    response_data = {}
    
    if request.method == 'POST' and form.is_valid():
        comment_form = form.cleaned_data['comment']
        comment_obj = Comment.objects.create(commented_on=content, user=request.user.userprofile, comment=comment_form)
    
    
    data_comment = Comment.objects.filter(commented_on=content)
    
    context = {
        'list_comment':data_comment,
        'content':content,
    }
    
    return render(request, "comments.html", context)


        
# butuh @
@login_required(login_url='/login/')
def delete(request, group_name, id):
    author_forum = Content.objects.get(id=id)
    
    # TODO: admin juga bsa ngehapus --> dafi
    if request.user == author_forum.creator.user :
        forum = Content.objects.get(id=id)
        forum.delete()
        return JsonResponse({'msg':'success'})
    else:
        # buat ngasih tau gagal, karena bukan authornya
        pass
    
    

# belum jadi
# butuh @
@login_required(login_url='/login/')
def upvote(request,group_name, content_id):
    content=Content.objects.get(id=content_id)
    if request.user.userprofile in content.contentupvote.upvoter.all():
        content.contentupvote.upvoter.remove(request.user.userprofile)
    else:
        content.contentupvote.upvoter.add(request.user.userprofile)
    jumlah_upvote = content.contentupvote.upvoter.distinct().count()
    
    return redirect(f"../../")