# Generated by Django 2.0.5 on 2018-10-13 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0004_hardwareassign_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareassign',
            name='return_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]