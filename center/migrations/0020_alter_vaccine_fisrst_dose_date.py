# Generated by Django 4.0 on 2021-12-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0019_remove_disease_center_remove_vaccine_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='fisrst_dose_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
