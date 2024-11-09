from django.urls import path
# from .views import list_books, LibraryDetailView

# urlpatterns = [
#     path('book list', list_books, name='list_books'),
#     path('library detail <int:library_id>', LibraryDetailView, name='library_detail'),
   
# ]
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', views.CustomLogoutView.as_view(), name='logout'),

]