# Generated by Django 2.0.5 on 2018-09-13 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0003_assets_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_staff', to='ams.Staff'),
        ),
    ]
