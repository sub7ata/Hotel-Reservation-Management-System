# Generated by Django 2.2.6 on 2019-10-19 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0019_auto_20191019_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 6, 19, 18, 880406)),
        ),
    ]