# Generated by Django 3.0.7 on 2020-06-17 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('getawayHolidays', '0003_auto_20200616_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=10, null=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=255, null=True)),
                ('marital_status', models.CharField(choices=[(0, 'single'), (1, 'married')], max_length=24)),
                ('spouse', models.CharField(max_length=255, null=True)),
                ('anniversary', models.DateTimeField()),
                ('gender', models.CharField(choices=[(0, 'Male'), (1, 'Female')], max_length=24)),
                ('city', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('client_signature', models.CharField(max_length=255)),
                ('signature_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('health_conditions', models.ManyToManyField(null=True, to='getawayHolidays.HealthConditions')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=6, max_digits=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.AlterField(
            model_name='reservations',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getawayHolidays.ClientsProfile'),
        ),
    ]
