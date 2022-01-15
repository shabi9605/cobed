# Generated by Django 4.0 on 2021-12-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0017_remove_patientstatus_test_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_status',
            field=models.CharField(blank=True, choices=[('death with in one month', 'death_with_in_onemonth'), ('discharged', 'discharged'), ('shifted to CFLTC', 'shifted_to_CFLTC'), ('shifted to CSLTC', 'shifted_to_CSLTC'), ('shifted_to_domociline', 'shifted_to_domociline'), ('shifted_to_home', 'shifted_to_home'), ('death', 'death'), ('positive', 'positive'), ('negative', 'negative')], max_length=30, null=True),
        ),
    ]
