from django.db import models

class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
