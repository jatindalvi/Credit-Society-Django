# Generated by Django 2.2 on 2019-11-01 13:44

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cdmonth',
            old_name='February',
            new_name='february',
        ),
        migrations.RenameField(
            model_name='sharemonth',
            old_name='February',
            new_name='february',
        ),
        migrations.AddField(
            model_name='cdmonth',
            name='year',
            field=models.IntegerField(blank=True, default=2019, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notidate',
            field=models.DateField(default=datetime.date(2019, 11, 1)),
        ),
        migrations.AlterUniqueTogether(
            name='cdmonth',
            unique_together={('username', 'year')},
        ),
        migrations.RemoveField(
            model_name='cdmonth',
            name='encode',
        ),
    ]