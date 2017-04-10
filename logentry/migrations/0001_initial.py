# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logentry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=20)),
                ('asctime', models.DateTimeField(null=True)),
                ('module', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('user', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
