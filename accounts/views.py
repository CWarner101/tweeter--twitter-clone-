"""
Name: Connor Warner
Class: CIS 218 
Date: 4/8/2024
"""


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView

from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUpView(CreateView):
    """Sign Up View"""
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
        return obj.pk == self.request.user.pk
    

class ProfilePublicView(LoginRequiredMixin, DetailView):
    """Profile Public Detail View"""

    model = CustomUser
    template_name = "registration/profile_public.html"