# Generated by Django 3.0.7 on 2020-06-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getawayHolidays', '0009_auto_20200623_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activities',
            name='restrict_conditions',
            field=models.ManyToManyField(blank=True, null=True, to='getawayHolidays.HealthConditions'),
        ),
    ]
