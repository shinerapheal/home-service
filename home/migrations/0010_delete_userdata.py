# Generated by Django 5.0 on 2024-06-20 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_login_userdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userdata',
        ),
    ]