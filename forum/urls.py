from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('json/', show_json, name='json'),
    path('<str:group_name>/json/', show_json_group, name='json_group'),
    path('create-post/', create_post, name='create-post'),
    path('create-forum/', create_group, name='create-group'),
    path('create-forum/name/', get_group_name, name='group-name'),
]