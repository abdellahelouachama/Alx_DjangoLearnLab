from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Store images in 'profile_pics/' folder
    bio = models.TextField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200, required=True)
    content = models.TextField(required=True, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

