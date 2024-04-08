"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django.urls import path

from .views import SignUpView, ProfileUpdateView, ProfilePublicView

urlpatterns = [
    path("profile/<int:pk>/", ProfileUpdateView.as_view(), name="profile_update"),
    path("profile_public/<int:pk>/", ProfilePublicView.as_view(), name="profile_public"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
