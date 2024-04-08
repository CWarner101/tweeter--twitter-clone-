"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
            )


class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
            )