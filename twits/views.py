from django.views.generic import (
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy

from .models import Twit

class TwitListView(ListView):
    """Twit List View"""
    
    model = Twit
    template_name = "twit_list.html"

class TwitDetailView(DetailView):
    """Twit Detail View"""

    model = Twit
    template_name = "twit_detail.html"

class TwitUpdateView(UpdateView):
    """Twit Detail View"""

    model = Twit
    fields = 'body',
    template_name = "twit_edit.html"

class TwitDeleteView(DeleteView):
    """Twit Detail View"""

    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")