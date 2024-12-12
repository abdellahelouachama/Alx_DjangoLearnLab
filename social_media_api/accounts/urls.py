from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserAPIView


urlpatterns = [
    # athentication url paths
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    
    # user profile management url paths
    path('profile/<username>', UserAPIView.as_view({'get': 'retrieve'}), name='profile'),
    path('profile/<username>', UserAPIView.as_view({'put': 'update'}), name='profile'),
    path('profile/<username>', UserAPIView.as_view({'patch': 'partial_update'}), name='profile'),
    path('profile/<username>', UserAPIView.as_view({'delete': 'destroy'}), name='profile'),

]