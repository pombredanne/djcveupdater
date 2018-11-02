# Generated by Django 2.1 on 2018-11-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updater_cpe', '0002_auto_20181101_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerability_cpe',
            name='component',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe',
            name='vendor',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe',
            name='version',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe_modified',
            name='component',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe_modified',
            name='vendor',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe_modified',
            name='version',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe_new',
            name='component',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe_new',
            name='vendor',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_cpe_new',
            name='version',
            field=models.TextField(default=''),
        ),
    ]
