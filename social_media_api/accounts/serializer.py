from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# serializer to handle user data conversion (serializing and deserializing)
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture']