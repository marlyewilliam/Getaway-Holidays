# Generated by Django 3.0.7 on 2020-06-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getawayHolidays', '0011_auto_20200623_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='activities',
        ),
        migrations.AddField(
            model_name='reservations',
            name='activities',
            field=models.ManyToManyField(null=True, to='getawayHolidays.Activities'),
        ),
    ]
