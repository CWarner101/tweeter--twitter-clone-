from django.urls import path

from .views import (
    TwitListView,
    TwitCommentView,
    TwitUpdateView,
    TwitDeleteView,
    TwitCreateView,
    TwitLikeView
)

urlpatterns = [
    path("<int:pk>/", TwitCommentView.as_view(), name="twit_comment"),
    path("<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("new/", TwitCreateView.as_view(), name="twit_new"),
    path("", TwitListView.as_view(), name="twit_list"),
]
