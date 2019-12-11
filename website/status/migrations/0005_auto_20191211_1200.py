# Generated by Django 2.2 on 2019-12-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20191211_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdmonth',
            name='encode',
        ),
        migrations.AddField(
            model_name='cdmonth',
            name='dividend',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='cdmonth',
            name='sum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='cdmonth',
            name='year',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]