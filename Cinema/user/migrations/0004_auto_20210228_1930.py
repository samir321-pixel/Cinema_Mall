# Generated by Django 3.1.7 on 2021-02-28 14:00

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_booking', '0008_auto_20210228_1502'),
        ('user', '0003_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='past_booking',
            field=models.ManyToManyField(to='cinema_booking.Seat'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(default='1231', max_length=31),
            preserve_default=False,
        ),
    ]
