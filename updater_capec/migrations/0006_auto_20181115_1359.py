# Generated by Django 2.1 on 2018-11-15 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updater_capec', '0005_auto_20181112_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vulnerability_capec',
            options={'ordering': ['capec_id', 'modification'], 'verbose_name': 'VULNERABILITY_CAPEC', 'verbose_name_plural': 'VULNERABILITY_CAPEC'},
        ),
    ]
