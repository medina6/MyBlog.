from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('profile/', views.ProfileView.as_view()),
    # path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view()),
]