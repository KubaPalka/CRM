# Generated by Django 4.2.1 on 2023-06-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0013_application_date_added_application_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='legalform',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
