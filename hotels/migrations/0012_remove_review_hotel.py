# Generated by Django 5.1.3 on 2024-12-04 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='hotel',
        ),
    ]