# Generated by Django 2.1 on 2018-11-05 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('updater_npm', '0009_auto_20181105_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='STATUS_NPM',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'STATUS_NPM',
                'verbose_name_plural': 'STATUS_NPMS',
            },
        ),
    ]
