# Generated by Django 5.1.3 on 2025-02-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0036_booked_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
