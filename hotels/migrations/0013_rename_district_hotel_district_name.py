# Generated by Django 5.1.3 on 2024-12-04 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0012_remove_review_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='district',
            new_name='district_name',
        ),
    ]
