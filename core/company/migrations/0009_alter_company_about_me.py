# Generated by Django 4.1 on 2022-08-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_company_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about_me',
            field=models.CharField(max_length=2550),
        ),
    ]
