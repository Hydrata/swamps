# Generated by Django 2.2.20 on 2021-07-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swamps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluemountainsthpsse448032756',
            name='overall_status',
            field=models.CharField(blank=True, default='unknown', max_length=256, null=True),
        ),
    ]
