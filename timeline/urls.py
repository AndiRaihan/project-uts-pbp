from django.urls import path
from timeline.views import *

app_name = 'timeline'

urlpatterns = [
    path('group/<str:group_name>/', show_timeline, name='timeline'),
    path('group/<str:group_name>/<int:content_id>/comment/', comment, name='comment'),
    path('group/<str:group_name>/<int:content_id>/comment/json/', comment_json, name='comment'),
    path('group/<str:group_name>/<int:content_id>/comment/add/', add_comment, name='comment'),
    path('', show_group, name='landing'),
    path('group/<str:group_name>/<int:content_id>/delete/', delete, name='delete'),
    path('group/<str:group_name>/<int:content_id>/upvote/', upvote, name='upvote'),
    path('show-group-json/', show_group_json, name="show-group-json"),
    
    path('group/<str:group_name>/json-flutter/', show_timeline_json, name='timeline'),
]