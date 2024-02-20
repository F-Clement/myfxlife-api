from django.db import models
from django.contrib.auth.models import User


# A notification model to notify users each time a profile they follow
# posts new content, a profile follows them, comments or likes a post they user owns.

class Notification(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.owner}'s notification"
