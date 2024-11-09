from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('book list', list_books, name='list_books'),
    path('library detail <int:library_id>', LibraryDetailView, name='library_detail'),
   
]
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns += [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

]

urlpatterns += [
    path('admin_view', views.Admin, name='librarian_view'),
    path('librarian_view', views.Librarian, name='librarian_view'),
    path('member_view', views.Member, name='member_view'),
]