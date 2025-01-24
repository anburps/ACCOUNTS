from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('profile/', views.UserProfileView.as_view()),
    path('user/', views.UserView.as_view()),
]
