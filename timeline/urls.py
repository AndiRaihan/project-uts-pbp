from django.urls import path
from timeline.views import *

app_name = 'timeline'

urlpatterns = [

    path('group/<str:group_name>/', show_timeline, name='timeline'),
    path('group/<str:group_name>/<int:content_id>/comment/', comment, name='comment'),
    path('', show_group, name='landing'),
    path('group/<str:group_name>/<int:content_id>/delete/', delete, name='delete'),
    path('group/<str:group_name>/<int:content_id>/upvote/', upvote, name='upvote'),
]