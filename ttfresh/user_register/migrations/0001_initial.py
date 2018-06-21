# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=20)),
                ('uemail', models.CharField(max_length=50)),
                ('uphone', models.CharField(max_length=11)),
                ('uaddress', models.CharField(max_length=100)),
                ('ucode', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
    ]
