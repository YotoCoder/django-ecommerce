# Generated by Django 4.1 on 2022-08-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_company_currency_alter_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='about_me',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]