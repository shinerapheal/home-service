# Generated by Django 5.0 on 2024-06-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_conf_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='type',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
