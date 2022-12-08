from django.urls import path
from authentication.views import login, register, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='json'),
    path('register/', register, name='signup'),
    path('logout/', logout, name='logout'),
]