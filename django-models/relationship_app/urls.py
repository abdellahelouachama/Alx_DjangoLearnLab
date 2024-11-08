from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/',views.list_books, name='list_books'),
    path('library detail/<int:library_id>', views.LibraryDetailView, name='library_detail'),
    path('login/', view=LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', view=LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register, name='register'),
]