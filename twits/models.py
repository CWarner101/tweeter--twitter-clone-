from django.conf import settings
from django.db import models
from django.urls import reverse

class Twit(models.Model):
    """Twit Post Model"""
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Twit as a string"""
        return self.body[:50]
    
    def get_absolute_url(self):
        """Absolute URL for twit"""
        return reverse("twit_detail", kwargs={"pk": self.pk})
    

class Comments(models.Model):
    """Comments on Twits"""

    twit = models.ForeignKey(
        Twit,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    comment = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)