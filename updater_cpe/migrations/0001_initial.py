# Generated by Django 2.1.2 on 2018-10-27 12:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VULNERABILITY_CPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpe_id', models.TextField(default='')),
                ('title', models.TextField(default='')),
                ('cpe_2_2', models.TextField(default='')),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'VULNERABILITY_CPE',
                'verbose_name_plural': 'VULNERABILITY_CPES',
                'ordering': ['cpe_id'],
            },
        ),
    ]