# Generated by Django 2.2.6 on 2019-10-19 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0009_auto_20191019_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 4, 45, 28, 172979)),
        ),
    ]