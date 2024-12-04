from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post, Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','password1', 'password2', 'email' , 'picture', 'bio')  


class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(max_length=500)  

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'picture', 'bio')       
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(attrs={'placeholder': 'Add tags, separated by commas'})
    )  # Use TagWidget here

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']