# Generated by Django 5.1.3 on 2025-02-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0042_booked_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='is_paid',
        ),
    ]
