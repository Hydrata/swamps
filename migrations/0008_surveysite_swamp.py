# Generated by Django 2.2.20 on 2021-10-05 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swamps', '0007_auto_20210930_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveysite',
            name='swamp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swamps.BluemountainsThpssE448032756'),
        ),
    ]