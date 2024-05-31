from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField("custom_user.CustomUser", on_delete=models.CASCADE)
    bio = models.TextField(blank=True)