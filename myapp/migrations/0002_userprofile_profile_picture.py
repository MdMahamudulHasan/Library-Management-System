# Generated by Django 5.0.1 on 2024-09-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]
