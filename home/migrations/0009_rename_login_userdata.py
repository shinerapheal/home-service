# Generated by Django 5.0 on 2024-06-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='userdata',
        ),
    ]