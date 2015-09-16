# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('peixeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPeixeiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=15, blank=True)),
                ('cpf', models.CharField(max_length=15, blank=True)),
                ('cnpj', models.CharField(max_length=30, blank=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
