# Generated by Django 5.1.6 on 2025-02-09 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0029_remove_booked_payment_booked_total_amount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=50)),
                ('Order', models.BooleanField(default=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('booked', models.ManyToManyField(to='hotels.booked')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
