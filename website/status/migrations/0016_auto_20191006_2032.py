# Generated by Django 2.2 on 2019-10-06 15:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0015_auto_20191005_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyloan',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notidate',
            field=models.DateField(default=datetime.date(2019, 10, 6)),
        ),
    ]