"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .forms import CustomUserCreationForm
from .models import CustomUser
from twits.models import Twit

class SignUpView(CreateView):
    """Sign Up View"""
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile Update View"""

    model = CustomUser
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'date_of_birth',
    )
    success_url = reverse_lazy("twit_list")
    template_name = "registration/profile_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    

class ProfilePublicView(LoginRequiredMixin, DetailView):
    """Profile Public Detail View"""

    model = CustomUser
    template_name = "registration/profile_public.html"