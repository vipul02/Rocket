# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_token', models.CharField(max_length=255)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=120, unique=True)),
                ('password', models.TextField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='sessionmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rapp.SignUpModel'),
        ),
    ]