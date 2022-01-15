# Generated by Django 4.0 on 2021-12-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_phone_home_phonenumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='working_time',
        ),
        migrations.AddField(
            model_name='lab',
            name='lab_district',
            field=models.CharField(blank=True, choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'), ('Alappuzha', 'Alappuzha'), ('Pathanamthitta', 'Pathanamthitta'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), (' Ernakulam', ' Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), (' Kozhikode', ' Kozhikode'), ('Wayanadu', 'Wayanadu'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], default='Thrissur', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='loaction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
