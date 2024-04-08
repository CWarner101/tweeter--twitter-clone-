"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django.contrib import admin

from .models import Twit, Comment

admin.site.register(Twit)
admin.site.register(Comment)
