from django.db import models

# Create your models here.

class Wish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='path/to/default/image.jpg')
    store = models.CharField(max_length=50)

    def __str__(self):
        return self.name
