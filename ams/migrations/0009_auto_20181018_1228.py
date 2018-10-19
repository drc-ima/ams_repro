# Generated by Django 2.0.5 on 2018-10-18 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0008_auto_20181014_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareassign',
            name='assign_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hardware_assign_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='informationassign',
            name='assign_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='information_assign_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='infrastructureassign',
            name='assign_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infrastructure_assign_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='softwareassign',
            name='assign_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='software_assign_by', to=settings.AUTH_USER_MODEL),
        ),
    ]