# Generated by Django 3.1.3 on 2020-11-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201128_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='scenario_step',
            field=models.IntegerField(default=0),
        ),
    ]