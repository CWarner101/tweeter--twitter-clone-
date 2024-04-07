from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Twit
from .forms import CommentForm


class TwitListView(LoginRequiredMixin, ListView):
    """Twit List View"""
    
    model = Twit
    template_name="twit_list.html"


class TwitDetailView(LoginRequiredMixin, View):
    """Twit Detail View"""

    def get(self, request, *args, **kwargs):
        """Doing GET request"""
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Doing POST request"""
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)
    
class CommentGetView(DetailView):
    """Comment Get View"""

    model = Twit
    template_name = "twit_detail.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the template"""
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPostView(SingleObjectMixin, FormView):
    """Comment Post View"""
    model = Twit
    form_class = CommentForm
    template_name = "twit_detail.html"

    def post(self, request, *args, **kwargs):
        # Get the Twit object
        self.object = self.get_object()
        # Do work parent would have
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """Create new comment when form is valid"""
        # Get the comment instance by saving the form with commit to False
        comment = form.save(commit=False)
        # Attach the artcle to the new comment.
        comment.twit = self.object
        # Attach the user to the new comment
        comment.author = self.request.user
        # Save the comment instance to the DB
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """Get the success url"""
        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk": twit.pk})


class TwitUpdateView(LoginRequiredMixin, UpdateView):
    """Twit Detail View"""

    model = Twit
    fields = 'body',
    template_name = "twit_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TwitDeleteView(LoginRequiredMixin, DeleteView):
    """Twit Detail View"""

    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")


class TwitCreateView(LoginRequiredMixin, CreateView):
    """Twit Create View"""

    model = Twit
    fields = ("body", "image_url")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    template_name="twit_new.html"


class TwitLikeView(LoginRequiredMixin, View):
    """Twit Like View"""
    def get(self, request, *args, **kwargs):
        """GET Request"""

        # Get out the data from the Get request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)

        twit = Twit.objects.get(id=twit_id)
        if twit_action == "like":
            # Do like stuff
            twit.likes.add(request.user)
        else:
            # Do unlike stuff
            twit.likes.remove(request.user)


        return JsonResponse(
            {
                "success":True
            }
        )
