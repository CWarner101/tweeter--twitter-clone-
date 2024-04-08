"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """Comment Form"""

    class Meta:
        model = Comment
        fields = ('comment',)