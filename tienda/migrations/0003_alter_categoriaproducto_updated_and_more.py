# Generated by Django 4.0 on 2022-04-20 04:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_remove_producto_categorias_producto_categoriasprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaproducto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default=datetime.datetime(2022, 4, 20, 4, 15, 35, 803672, tzinfo=utc), upload_to='tienda'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]