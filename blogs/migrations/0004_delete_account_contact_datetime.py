# Generated by Django 4.1.2 on 2022-10-31 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
