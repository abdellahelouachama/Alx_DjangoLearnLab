from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializer import UserSerializer
from .permission import IsLoggedIn
from rest_framework import status
User = get_user_model()

# register view to handle user creation
class RegisterView(APIView):

    def post(self, request):
        
        """
        Handle the creation of a new user.

        Args:
            request (Request): The request body with the user details.

        Returns:
            Response: A response with the result of the registration.

        Raises:
            Exception: If the registration of the user failed.
        """
        
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        profile_picture = request.data.get('profile_picture', None)
        bio = request.data.get('bio', '')

        if not username or not email or not password:
            return Response({'error': 'Username, Email, Password, are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                profile_picture=profile_picture,
                bio=bio
            )
            return Response({'message':'User registered successfully.'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# login view to handle credentials validation and token generation
class LoginView(APIView):  

    def post(self, request):
        """
        Handle the login of a user.

        Args:
            request (Request): The request body with the user credentials.

        Returns:
            Response: A response with the result of the login and token.

        Raises:
            Exception: If the login of the user failed.
        """

        username = request.data.get('username') 
        password = request.data.get('password') 

        if not username and not password:
            return Response({'error':'Username and Password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request=request, username=username, password=password)

        if user is not None:

            token, created = Token.objects.get_or_create(user=user)
            return Response(
                        {
                            'message': 'Login successful', 
                            'token': token.key
                        }, 
                            status=status.HTTP_200_OK 
                        )
        
        return Response({'error':'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

# logout view to handle logout operation and token deletion
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handle the logout of a user by deleting the authentication token.

        Args:
            request (Request): The request object containing the user information.

        Returns:
            Response: A response indicating the success or failure of the logout operation.
        """

        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message':'Logout seccussful'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Token does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

# user viewset to handle profile managment(reterive, update, delete)
# note : user creation handled in RegisterView
class UserAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsLoggedIn]
    lookup_field = 'username'

    def get_object(self):
        """
    Retrieve and return the user object based on the username lookup field.

    Checks the permissions for the retrieved object before returning it.

    Returns:
        User: The user object if permissions are granted and the object is found.
        """
        obj =  super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
    
    def destroy(self, request, *args, **kwargs):
        """
    Custom destroy method to return a 200 status code with a success message
    instead of the default 204 status code with an empty response.

    Args:
        request: The request object
        *args: Additional positional arguments
        **kwargs: Additional keyword arguments

    Returns:
        Response: A response with a success message and a 200 status code
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Deleted successfully."}, 
            status=status.HTTP_200_OK
        )

    def perform_destroy(self, instance):
        """
        Destroy the given user object.

        Args:
            instance: The user object to be deleted
        """
        instance.delete()