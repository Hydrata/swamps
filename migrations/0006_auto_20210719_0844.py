# Generated by Django 2.2.20 on 2021-07-19 08:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swamps', '0005_auto_20210718_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveysite',
            name='activities',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
