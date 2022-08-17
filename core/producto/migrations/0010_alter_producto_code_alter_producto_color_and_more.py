# Generated by Django 4.1 on 2022-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0009_category_remove_producto_offer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/productos/'),
        ),
    ]
