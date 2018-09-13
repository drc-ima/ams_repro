# Generated by Django 2.0.5 on 2018-09-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0004_department_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='staff',
        ),
        migrations.AddField(
            model_name='department',
            name='staff',
            field=models.ManyToManyField(related_name='department_staff', to='ams.Staff'),
        ),
    ]