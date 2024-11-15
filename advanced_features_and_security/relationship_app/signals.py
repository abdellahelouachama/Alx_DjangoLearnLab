from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import UserProfile, Book  # Adjust if these models are in different apps

@receiver(post_save, sender=User)
def assign_role_permissions(sender, instance, created, **kwargs):
    if created:
        # Assign a role based on your condition
        role = 'Admin'  # or 'Librarian', 'Member', based on your logic
        user_profile = UserProfile.objects.create(user=instance, role=role)

        # Retrieve permissions associated with this role
        permissions = UserProfile.PERMISSIONS_BY_ROLE.get(role, [])
        
        # Assign permissions to the user
        content_type = ContentType.objects.get_for_model(Book)
        for permission_codename in permissions:
            try:
                permission = Permission.objects.get(codename=permission_codename, content_type=content_type)
                instance.user_permissions.add(permission)
            except Permission.DoesNotExist:
                pass  # Handle cases where permission doesn't exist
