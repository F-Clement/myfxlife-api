# Generated by Django 3.2.24 on 2024-02-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_iaceh6', upload_to='images/'),
        ),
    ]
