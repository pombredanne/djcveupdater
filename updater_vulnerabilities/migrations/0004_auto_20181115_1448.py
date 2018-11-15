# Generated by Django 2.1 on 2018-11-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updater_cpe', '0007_auto_20181112_1256'),
        ('updater_capec', '0006_auto_20181115_1359'),
        ('updater_snyk', '0004_auto_20181113_1343'),
        ('updater_cwe', '0007_auto_20181112_1620'),
        ('updater_cve', '0006_auto_20181115_1359'),
        ('updater_npm', '0015_auto_20181112_1652'),
        ('updater_vulnerabilities', '0003_auto_20181115_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerabilities',
            name='capecs',
        ),
        migrations.AddField(
            model_name='vulnerabilities',
            name='capecs',
            field=models.ManyToManyField(to='updater_capec.VULNERABILITY_CAPEC'),
        ),
        migrations.RemoveField(
            model_name='vulnerabilities',
            name='cpes',
        ),
        migrations.AddField(
            model_name='vulnerabilities',
            name='cpes',
            field=models.ManyToManyField(to='updater_cpe.VULNERABILITY_CPE'),
        ),
        migrations.RemoveField(
            model_name='vulnerabilities',
            name='cves',
        ),
        migrations.AddField(
            model_name='vulnerabilities',
            name='cves',
            field=models.ManyToManyField(to='updater_cve.VULNERABILITY_CVE'),
        ),
        migrations.RemoveField(
            model_name='vulnerabilities',
            name='cwes',
        ),
        migrations.AddField(
            model_name='vulnerabilities',
            name='cwes',
            field=models.ManyToManyField(to='updater_cwe.VULNERABILITY_CWE'),
        ),
        migrations.RemoveField(
            model_name='vulnerabilities',
            name='npms',
        ),
        migrations.AddField(
            model_name='vulnerabilities',
            name='npms',
            field=models.ManyToManyField(to='updater_npm.VULNERABILITY_NPM'),
        ),
        migrations.RemoveField(
            model_name='vulnerabilities',
            name='snyks',
        ),
        migrations.AddField(
            model_name='vulnerabilities',
            name='snyks',
            field=models.ManyToManyField(to='updater_snyk.VULNERABILITY_SNYK'),
        ),
    ]
