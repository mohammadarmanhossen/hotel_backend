# Generated by Django 5.1.3 on 2025-01-01 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0022_alter_review_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='hotel',
        ),
    ]
