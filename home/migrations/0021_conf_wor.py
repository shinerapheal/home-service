# Generated by Django 5.0 on 2024-08-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_customer_info_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='conf',
            name='wor',
            field=models.CharField(default='no data', max_length=50),
        ),
    ]
