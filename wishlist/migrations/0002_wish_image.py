# Generated by Django 4.2.20 on 2025-04-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='image',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='images/'),
        ),
    ]
