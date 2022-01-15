# Generated by Django 3.2.6 on 2021-12-20 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_dmo_status_appruval'),
        ('patient', '0003_chat_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.doctor'),
        ),
    ]
