# Generated by Django 5.1.6 on 2025-02-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='Order',
        ),
    ]
