# Generated by Django 2.0.5 on 2018-11-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0008_auto_20181108_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='image',
            field=models.ImageField(blank=True, upload_to='hard_photo'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='image',
            field=models.ImageField(blank=True, upload_to='infras_photo'),
        ),
        migrations.AlterField(
            model_name='software',
            name='image',
            field=models.ImageField(blank=True, upload_to='soft_photo'),
        ),
    ]