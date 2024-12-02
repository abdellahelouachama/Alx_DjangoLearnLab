from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    picture = forms.ImageField()
    bio = forms.Textarea()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fiedls = ('username', 'email', 'picture', 'bio')
        
class CustomUserChangeForm(UserChangeForm):
    profile_bio = forms.CharField(max_length=500, required=False)  # Example of custom field

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'picture', 'bio')
        