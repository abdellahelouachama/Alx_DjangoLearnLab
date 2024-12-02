from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    picture = forms.ImageField(required=False)
    bio = forms.Textarea(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'picture', 'bio')  


class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(max_length=500, required=False)  # Use existing field

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'picture', 'bio')        