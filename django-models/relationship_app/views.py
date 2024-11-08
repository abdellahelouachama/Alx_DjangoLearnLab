from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(decorator)

@role_required('Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@role_required('Member')
def member_view(request):
    return render(request, 'member_view.html')
