# Generated by Django 2.1 on 2018-11-08 13:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import updater_cve.models


class Migration(migrations.Migration):

    dependencies = [
        ('updater_cve', '0002_vulnerability_cve_modified_vulnerability_cve_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerability_cve',
            name='access',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=updater_cve.models.default_access),
        ),
        migrations.AlterField(
            model_name='vulnerability_cve',
            name='impact',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=updater_cve.models.default_impact),
        ),
        migrations.AlterField(
            model_name='vulnerability_cve_modified',
            name='access',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=updater_cve.models.default_access),
        ),
        migrations.AlterField(
            model_name='vulnerability_cve_modified',
            name='impact',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=updater_cve.models.default_impact),
        ),
        migrations.AlterField(
            model_name='vulnerability_cve_new',
            name='access',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=updater_cve.models.default_access),
        ),
        migrations.AlterField(
            model_name='vulnerability_cve_new',
            name='impact',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=updater_cve.models.default_impact),
        ),
    ]
