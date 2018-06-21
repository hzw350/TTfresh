# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0003_auto_20180606_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiverInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rname', models.CharField(max_length=20)),
                ('raddress', models.CharField(max_length=20)),
                ('rcode', models.CharField(max_length=6)),
                ('rphone', models.CharField(max_length=11)),
                ('ruser', models.ForeignKey(to='user_register.UserInfo')),
            ],
            options={
                'db_table': 'ReceiverInfo',
            },
        ),
    ]
