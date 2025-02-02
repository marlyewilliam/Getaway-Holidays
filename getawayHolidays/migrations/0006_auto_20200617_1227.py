# Generated by Django 3.0.7 on 2020-06-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getawayHolidays', '0005_auto_20200617_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsprofile',
            name='anniversary',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='clientsprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=24),
        ),
        migrations.AlterField(
            model_name='clientsprofile',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=24),
        ),
    ]
