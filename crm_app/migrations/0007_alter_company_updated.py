# Generated by Django 4.2.1 on 2023-05-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0006_alter_company_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='updated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
