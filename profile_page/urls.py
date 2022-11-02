from django.urls import path
from profile_page.views import *

app_name = 'profile_page'

urlpatterns = [
    path('myprofile/', show_my_profile, name='my-profile'),
    path('myprofile/json', get_my_profile_json, name='get_my_profile_json'),
    path('myprofile/edit', edit_my_profile, name="edit-my-profile")
]