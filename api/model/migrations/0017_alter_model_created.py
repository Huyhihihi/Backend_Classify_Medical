# Generated by Django 3.2.5 on 2024-05-26 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_label', '0016_alter_model_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 5, 26, 19, 15, 59, 863758)),
        ),
    ]
