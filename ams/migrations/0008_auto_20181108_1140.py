# Generated by Django 2.0.5 on 2018-11-08 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ams', '0007_auto_20181108_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hardware_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='information',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='information_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='infrastructure',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infrastructure_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='software',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='software_admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
