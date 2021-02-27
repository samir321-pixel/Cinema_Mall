# Generated by Django 3.1.7 on 2021-02-27 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_booking', '0009_auto_20210227_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='date_slots',
            field=models.ForeignKey(default=25, on_delete=django.db.models.deletion.CASCADE, to='cinema_booking.available_slots'),
            preserve_default=False,
        ),
    ]
