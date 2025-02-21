# Generated by Django 5.1.3 on 2025-02-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0031_remove_booked_is_paid_remove_booked_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booked',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
    ]
