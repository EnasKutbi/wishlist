from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    wishlist = models.OneToOneField('wishlist.Wish', on_delete=models.CASCADE, null=True, blank=True, related_name='owner')
    friends = models.ManyToManyField('self', symmetrical=False, related_name='friend_set', blank=True)

    # Adding the related_name attributes for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',  # Make this unique to prevent clashes
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_set_permissions',  # Make this unique to prevent clashes
        blank=True,
    )

    def __str__(self):
        return self.username
