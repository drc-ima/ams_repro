# Generated by Django 2.0.5 on 2018-11-11 18:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0011_auto_20181111_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareassign',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='assets', unique=True),
        ),
    ]
