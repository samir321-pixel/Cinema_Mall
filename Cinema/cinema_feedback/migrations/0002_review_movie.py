# Generated by Django 3.1.7 on 2021-03-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managecinema', '0001_initial'),
        ('cinema_feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='managecinema.cinema'),
        ),
    ]
