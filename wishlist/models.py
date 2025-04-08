from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Wish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='path/to/default/image.jpg')
    store = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishes')  # link wishes to users

    def __str__(self):
        return self.name