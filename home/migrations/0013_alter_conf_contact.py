# Generated by Django 5.0 on 2024-06-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_conf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
