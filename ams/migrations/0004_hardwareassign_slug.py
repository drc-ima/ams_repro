# Generated by Django 2.0.5 on 2018-10-13 21:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0003_auto_20181013_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardwareassign',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='assets', unique=True),
        ),
    ]
