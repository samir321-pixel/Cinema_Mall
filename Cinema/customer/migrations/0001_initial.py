# Generated by Django 3.1.7 on 2021-02-28 08:10

from django.db import migrations, models
import localflavor.in_.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=30)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('state', localflavor.in_.models.INStateField(blank=True, max_length=2, null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
