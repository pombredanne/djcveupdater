# Generated by Django 2.1 on 2018-11-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VULNERABILITY_CWE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cwe_id', models.TextField(unique=True)),
                ('name', models.TextField(default='')),
                ('status', models.TextField(default='')),
                ('weakness', models.TextField(default='')),
                ('description_summary', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'VULNERABILITY_CWE',
                'verbose_name_plural': 'VULNERABILITY_CWES',
                'ordering': ['cwe_id'],
            },
        ),
        migrations.CreateModel(
            name='VULNERABILITY_CWE_MODIFIED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cwe_id', models.TextField(unique=True)),
                ('name', models.TextField(default='')),
                ('status', models.TextField(default='')),
                ('weakness', models.TextField(default='')),
                ('description_summary', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'VULNERABILITY_CWE_MODIFIED',
                'verbose_name_plural': 'VULNERABILITY_CWES_MODIFIED',
                'ordering': ['cwe_id'],
            },
        ),
        migrations.CreateModel(
            name='VULNERABILITY_CWE_NEW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cwe_id', models.TextField(unique=True)),
                ('name', models.TextField(default='')),
                ('status', models.TextField(default='')),
                ('weakness', models.TextField(default='')),
                ('description_summary', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'VULNERABILITY_CWE_NEW',
                'verbose_name_plural': 'VULNERABILITY_CWES_NEW',
                'ordering': ['cwe_id'],
            },
        ),
    ]
