# Generated by Django 2.0.5 on 2018-10-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='purchase_date',
            field=models.DateField(blank=True, default=''),
        ),
    ]