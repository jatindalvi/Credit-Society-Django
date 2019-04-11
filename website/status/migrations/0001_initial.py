# Generated by Django 2.1.7 on 2019-04-03 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnumber', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('sapid', models.IntegerField(unique=True)),
                ('dateofjoining', models.DateField()),
                ('shareamount', models.IntegerField(default=0)),
                ('sharebalance', models.IntegerField(default=0)),
                ('sharedividend', models.FloatField(blank=True, null=True)),
                ('cdamount', models.IntegerField(default=0)),
                ('cddividend', models.FloatField(blank=True, null=True)),
                ('cdbalance', models.IntegerField(default=0)),
                ('totalamount', models.IntegerField(default=0)),
                ('sharesstartingnumber', models.IntegerField(null=True)),
                ('sharesendingnumber', models.IntegerField(null=True)),
                ('isloantaken', models.BooleanField(default=False)),
                ('longloanamount', models.IntegerField(blank=True, null=True)),
                ('longloanprinciple', models.IntegerField(blank=True, null=True)),
                ('longloaninterest', models.FloatField(blank=True, null=True)),
                ('longloaninterestamount', models.IntegerField(blank=True, null=True)),
                ('longloanbalance', models.IntegerField(blank=True, null=True)),
                ('longloanemi', models.IntegerField(blank=True, null=True)),
                ('emerloanamount', models.IntegerField(blank=True, null=True)),
                ('emerloanprinciple', models.IntegerField(blank=True, null=True)),
                ('emerloaninterest', models.FloatField(blank=True, null=True)),
                ('emerloaninterestamount', models.IntegerField(blank=True, null=True)),
                ('emerloanbalance', models.IntegerField(blank=True, null=True)),
                ('emerloanemi', models.IntegerField(blank=True, null=True)),
                ('fdcapital', models.IntegerField(default=True, null=True)),
                ('fdmaturitydate', models.DateField(null=True)),
                ('fdinterest', models.FloatField(blank=True, null=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
