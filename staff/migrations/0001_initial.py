# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='people_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.People'),
        ),
    ]
