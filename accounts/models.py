from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    wishlist = models.OneToOneField('wishlist.Wish', on_delete=models.CASCADE, null=True, blank=True)
    friends = models.ManyToManyField('self', symmetrical=False, related_name='friend_set', blank=True)

    # Define the related_name for groups and user_permissions to avoid clash
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Change this to resolve clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Change this to resolve clash
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username