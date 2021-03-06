# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0009_remove_shift_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shift',
            name='locker',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shift.Locker'),
        ),
    ]
