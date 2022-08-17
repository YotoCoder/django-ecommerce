# Generated by Django 4.1 on 2022-08-17 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_company_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_simbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='about_me',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.currency'),
        ),
    ]
