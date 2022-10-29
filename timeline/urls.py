from django.urls import path
from timeline.views import *

app_name = 'timeline'

urlpatterns = [
    path('<str:group_name>', show_timeline, name='timeline'),
    path('<str:group_name>/<int:content_id>/comment', comment, name='comment'),
    path('', show_group, name='landing'),
    path('<str:group_name>/<int:content_id>/delete', delete, name='delete'),
    path('<str:group_name>/<int:content_id>/upvote', upvote, name='upvote'),
]