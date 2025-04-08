from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    wishlist = models.OneToOneField('wishlist.Wish', on_delete=models.SET_NULL, null=True, blank=True, related_name='owner')
    friends = models.ManyToManyField('User', symmetrical=False, related_name='friends_of', blank=True)

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

    def get_friends(self):
        return self.friends.all()
