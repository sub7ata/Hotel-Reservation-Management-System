# Generated by Django 2.2.6 on 2019-10-24 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0048_auto_20191024_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 3, 45, 11, 200490)),
        ),
    ]