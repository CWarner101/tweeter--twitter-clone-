from django.urls import path

from .views import (
    TwitListView,
    TwitDetailView,
    TwitUpdateView,
    TwitDeleteView,
)

urlpatterns = [
    path("<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("<int:pk>/edit", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete", TwitDeleteView.as_view(), name="twit_delete"),
    path("", TwitListView.as_view(), name="twit_list"),
]
