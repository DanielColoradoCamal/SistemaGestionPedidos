# Generated by Django 4.0 on 2022-04-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tienda'),
        ),
    ]