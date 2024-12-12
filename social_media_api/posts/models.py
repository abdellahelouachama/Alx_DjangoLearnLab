from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# post model 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    