# Generated by Django 4.0 on 2022-04-20 05:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default=datetime.datetime(2022, 4, 20, 5, 47, 44, 936720, tzinfo=utc), upload_to='blog'),
            preserve_default=False,
        ),
    ]
