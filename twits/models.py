from django.conf import settings
from django.db import models
from django.urls import reverse

class Twit(models.Model):
    """Twit Post Model"""
    body = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='twits',
    )
    
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_twits",
        blank=True,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        """Twit as a string"""
        return self.body[:50]
    
    def get_absolute_url(self):
        """Absolute URL for twit"""
        return reverse("twit_list")
    
    def get_like_url(self):
        """Get like URL based on pk"""
        return reverse("twit_like", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    """Comments Model"""

    twit = models.ForeignKey(
        Twit,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    comment = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Comment as a string"""
        return self.comment

    def get_absolute_url(self):
        """Comment absolute URL"""
        return reverse("twit_list")