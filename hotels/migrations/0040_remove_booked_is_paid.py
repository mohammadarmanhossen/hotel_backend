# Generated by Django 5.1.3 on 2025-02-13 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0039_booked_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='is_paid',
        ),
    ]
