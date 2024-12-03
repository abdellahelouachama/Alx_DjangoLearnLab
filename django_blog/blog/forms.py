from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    picture = forms.ImageField()
    bio = forms.Textarea()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'picture', 'bio')  


class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(max_length=500, required=False)  # Use existing field

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'picture', 'bio')       
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']