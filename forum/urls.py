from django.urls import path
from forum.views import *
from timeline.views import delete, upvote, upvote_ajax, comment, add_comment, comment_json

app_name = 'forum'

urlpatterns = [
    path('json/', show_json, name='json'),
    path('group/<str:group_name>/json/', show_json_group, name='json_group'),
    path('create-post/', create_post, name='create-post'),
    path('create-forum/', create_group, name='create-group'),
    path('create-forum/name/', get_group_name, name='group-name'),
    path('mypost/', show_my_post, name='my-post'),
    path('mypost/json/', show_my_post_json, name="my-post-json"),
    path('mypost/<int:content_id>/delete/', delete_post, name='delete'),
    path('mypost/<int:content_id>/upvote/', upvote_ajax, name='mypost-upvote'),
    path('mypost/<int:content_id>/comment/', comment, name='mypost-comment'),
    path('mypost/<int:content_id>/comment/json/', comment_json, name='mypost-comment'),
    path('mypost/<int:content_id>/comment/add/', add_comment, name='mypost-comment'),
    path('mypost/<int:content_id>/edit/', edit_post, name='mypost-edit'),
]