# Generated by Django 3.2.23 on 2024-02-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_y0zwt9', upload_to='images/'),
        ),
    ]
