from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view,register,update_user,update_user_profile

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',LogoutView.as_view(template_name='Users/logout.html')),
    path('signup/',register),
    path('update/',update_user),
    path('update/profile/',update_user_profile,name='profile'),

]