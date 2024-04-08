"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom User Model"""

    date_of_birth = models.DateField(null=True, blank=True)
    

