# Generated by Django 2.1 on 2018-11-05 08:26

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('updater_npm', '0007_auto_20181105_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vulnerability_npm_modified',
            options={'ordering': ['npm_id'], 'verbose_name': 'VULNERABILITY_NPM_MODIFIED', 'verbose_name_plural': 'VULNERABILITY_NPMS_MODIFIED'},
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='allowwd_scopes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='author',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='cves',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='cvss_code',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='cvss_vector',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='cwe',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='legacy_slug',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='module_name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='npm_id',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='overview',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='recommendation',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='references',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='slug',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='source',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vulnerability_npm_modified',
            name='vulnerable_versions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None),
        ),
    ]
