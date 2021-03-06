from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # why symmetrical false?
    # rsa: https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ManyToManyField
    friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')

    # keep track of posts liked by user
    likes = models.ManyToManyField('Post', blank=True, related_name='fans')

class Post(models.Model):
    """Represent a new post that has a content, timestamps (created/updated)
    and a user
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        # return posts in reverse chronological order (ie. most recent first)
        ordering = ['-created_at']

    def __str__(self):
        return f'Post ({self.id}): {self.content[:50]}'
