# Generated by Django 4.0 on 2021-12-19 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0012_alter_bed_bed_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bed',
            name='patient_status',
        ),
        migrations.AddField(
            model_name='bed',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='center.patient'),
        ),
        migrations.AddField(
            model_name='patientstatus',
            name='bed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='center.bed'),
        ),
    ]
