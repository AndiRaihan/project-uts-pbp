from django.urls import path, include
from authen.views import register
from authen.views import login_user
    
app_name = "authen"
urlpatterns = [
    path('register/', register, name='register'),
    path('', login_user, name='login'),
]
