from django.urls import path

from User_Authentication.views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    path('profile/update/', UserProfileUpdate.as_view(), name='user-profile-update'),
]
