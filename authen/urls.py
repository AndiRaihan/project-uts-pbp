from django.urls import path, include
from authen.views import register, logout_user, login_user
    
app_name = "authen"
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]
