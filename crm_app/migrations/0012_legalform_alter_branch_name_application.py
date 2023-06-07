# Generated by Django 4.2.1 on 2023-05-30 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0011_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('spółka akcyjna', 'spółka akcyjna'), ('spółka z o.o.', 'spółka z o.o.'), ('spółka komandytowa', 'spółka komandytowa'), ('spółka jawna', 'spółka jawna'), ('spółka cywilna', 'spółka cywilna'), ('1-os. DG', '1-os. DG'), ('spółdzielnia', 'spółdzielnia'), ('spółka komunalna', 'spółka komunalna'), ('wspólnota', 'wspólnota'), ('inna', 'inna')], max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(choices=[('administracja', 'administracja'), ('budownictwo', 'budownictwo'), ('handel', 'handel'), ('IT', 'IT'), ('ochrona zdrowia', 'ochrona zdrowia'), ('produkcja', 'produkcja'), ('przemysł', 'przemysł'), ('transport', 'transport'), ('usługi', 'usługi'), ('inne', 'inne')], max_length=32),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_number', models.CharField(max_length=16)),
                ('kwh_amount', models.CharField(max_length=16)),
                ('installation_type', models.CharField(choices=[('Skośny', 'Skośny'), ('Ekierka', 'Ekierka'), ('Balast WZ', 'Balast WZ'), ('Balast południe', 'Balast południe'), ('Klejona WZ', 'Klejona WZ'), ('Klejona Południe', 'Klejona Południe'), ('Grunt Mono', 'Grunt Mono'), ('Grunt Bifacial', 'Grunt Bifacial'), ('Carport Standard', 'Carport Standard'), ('Carport Premium', 'Carport Premium')], max_length=32)),
                ('panel_type', models.CharField(choices=[('Seraphim', 'Seraphim'), ('JA solar', 'JA solar'), ('Jinko', 'Jinko'), ('AE Solar', 'AE Solar'), ('Longi', 'Longi'), ('Trina', 'Trina'), ('Risen', 'Risen')], max_length=32)),
                ('payment', models.CharField(choices=[('SUSI', 'SUSI'), ('Leasing', 'Leasing'), ('Kredyt', 'Kredyt'), ('Gotówka', 'Gotówka')], max_length=32)),
                ('status', models.CharField(choices=[('złożony', 'złożony'), ('umowa', 'umowa'), ('wypłata', 'wypłata'), ('rezygnacja', 'rezygnacja')], max_length=16)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.company')),
            ],
        ),
    ]
