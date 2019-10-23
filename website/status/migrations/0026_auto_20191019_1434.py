# Generated by Django 2.2 on 2019-10-19 09:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0025_auto_20191011_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notidate',
            field=models.DateField(default=datetime.date(2019, 10, 19)),
        ),
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_encode', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('cd_encode', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('year', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sharemonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jan', models.IntegerField(blank=True, default=0, null=True)),
                ('feb', models.IntegerField(blank=True, default=0, null=True)),
                ('mar', models.IntegerField(blank=True, default=0, null=True)),
                ('apr', models.IntegerField(blank=True, default=0, null=True)),
                ('may', models.IntegerField(blank=True, default=0, null=True)),
                ('jun', models.IntegerField(blank=True, default=0, null=True)),
                ('jul', models.IntegerField(blank=True, default=0, null=True)),
                ('aug', models.IntegerField(blank=True, default=0, null=True)),
                ('sep', models.IntegerField(blank=True, default=0, null=True)),
                ('oct', models.IntegerField(blank=True, default=0, null=True)),
                ('nov', models.IntegerField(blank=True, default=0, null=True)),
                ('dec', models.IntegerField(blank=True, default=0, null=True)),
                ('encode', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cdmonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jan', models.IntegerField(blank=True, default=0, null=True)),
                ('feb', models.IntegerField(blank=True, default=0, null=True)),
                ('mar', models.IntegerField(blank=True, default=0, null=True)),
                ('apr', models.IntegerField(blank=True, default=0, null=True)),
                ('may', models.IntegerField(blank=True, default=0, null=True)),
                ('jun', models.IntegerField(blank=True, default=0, null=True)),
                ('jul', models.IntegerField(blank=True, default=0, null=True)),
                ('aug', models.IntegerField(blank=True, default=0, null=True)),
                ('sep', models.IntegerField(blank=True, default=0, null=True)),
                ('oct', models.IntegerField(blank=True, default=0, null=True)),
                ('nov', models.IntegerField(blank=True, default=0, null=True)),
                ('dec', models.IntegerField(blank=True, default=0, null=True)),
                ('encode', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
