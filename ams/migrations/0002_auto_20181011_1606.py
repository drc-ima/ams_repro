# Generated by Django 2.0.5 on 2018-10-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='attachment',
        ),
        migrations.AddField(
            model_name='information',
            name='file_type',
            field=models.CharField(blank=True, choices=[('doc', 'doc'), ('docx', 'docx'), ('xls', 'xls'), ('pptx', 'pptx'), ('others', 'others')], max_length=255),
        ),
    ]