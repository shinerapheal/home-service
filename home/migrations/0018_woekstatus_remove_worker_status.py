# Generated by Django 5.0 on 2024-08-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_worker_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='woekstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='worker',
            name='status',
        ),
    ]
