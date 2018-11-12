# Generated by Django 2.1 on 2018-11-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updater_cve', '0004_status_cve_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VULNERABILITY_CVE_MODIFIED',
        ),
        migrations.DeleteModel(
            name='VULNERABILITY_CVE_NEW',
        ),
        migrations.AddField(
            model_name='vulnerability_cve',
            name='modification',
            field=models.IntegerField(default=0),
        ),
    ]