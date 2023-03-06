# apps/user/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserSignUpView, UserSignInView, UserWithdrawalView

from django.contrib.auth import views as auth_views
from . import views


router = DefaultRouter()

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/', views.UserSignInView.as_view(), name = 'signup'),

    path('', include(router.urls)),
    path("sign-up/", UserSignUpView.as_view()),
    path("sign-in/", UserSignInView.as_view()),
    path("<int:pk>/withdraw/", UserWithdrawalView.as_view()),
]