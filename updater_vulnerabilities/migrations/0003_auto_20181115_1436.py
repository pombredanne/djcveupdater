# Generated by Django 2.1 on 2018-11-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('updater_vulnerabilities', '0002_auto_20181115_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerabilities',
            name='capecs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='updater_capec.VULNERABILITY_CAPEC'),
        ),
        migrations.AlterField(
            model_name='vulnerabilities',
            name='cpes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='updater_cpe.VULNERABILITY_CPE'),
        ),
        migrations.AlterField(
            model_name='vulnerabilities',
            name='cves',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='updater_cve.VULNERABILITY_CVE'),
        ),
        migrations.AlterField(
            model_name='vulnerabilities',
            name='cwes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='updater_cwe.VULNERABILITY_CWE'),
        ),
        migrations.AlterField(
            model_name='vulnerabilities',
            name='npms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='updater_npm.VULNERABILITY_NPM'),
        ),
        migrations.AlterField(
            model_name='vulnerabilities',
            name='snyks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='updater_snyk.VULNERABILITY_SNYK'),
        ),
    ]