# Generated by Django 4.1 on 2022-08-17 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_currency_alter_company_about_me_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.currency'),
        ),
    ]
