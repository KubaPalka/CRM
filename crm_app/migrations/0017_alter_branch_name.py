# Generated by Django 4.2.1 on 2023-06-01 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0016_alter_legalform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(choices=[('administracja', 'administracja'), ('budownictwo', 'budownictwo'), ('handel', 'handel'), ('IT', 'IT'), ('ochrona zdrowia', 'ochrona zdrowia'), ('produkcja', 'produkcja'), ('przemysł', 'przemysł'), ('transport', 'transport'), ('usługi', 'usługi'), ('inne', 'inne')], max_length=32),
        ),
    ]
