# Generated by Django 4.1 on 2022-08-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_rename_company_company_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nombre',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
