from django.urls import path
from profile_page.views import *

app_name = 'profile_page'

urlpatterns = [
    path('myprofile/', show_my_profile, name='my-profile'),
]