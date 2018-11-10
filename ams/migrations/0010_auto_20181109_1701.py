# Generated by Django 2.0.5 on 2018-11-09 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ams', '0009_auto_20181108_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_allocated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('allocated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allocated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='department',
        ),
        migrations.AddField(
            model_name='allocation',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allocate_department', to='ams.Department'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allocate_staff', to='ams.Staff'),
        ),
        migrations.AddField(
            model_name='department',
            name='staff',
            field=models.ManyToManyField(related_name='department_staff', through='ams.Allocation', to='ams.Staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ManyToManyField(related_name='staff_department', through='ams.Allocation', to='ams.Department'),
        ),
    ]
