# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('image', models.ImageField(upload_to=b'some_dir')),
                ('text', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Value',
                'verbose_name_plural': 'Values',
            },
        ),
    ]
