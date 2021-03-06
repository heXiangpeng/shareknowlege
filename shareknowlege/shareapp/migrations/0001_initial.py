# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 03:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('articleid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('smallcontent', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classfication',
            fields=[
                ('classid', models.AutoField(primary_key=True, serialize=False)),
                ('classname', models.CharField(max_length=30, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='commnent',
            fields=[
                ('commnentid', models.AutoField(primary_key=True, serialize=False)),
                ('articleid', models.IntegerField()),
                ('commnenttext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='name')),
                ('password', models.CharField(max_length=20, verbose_name='pass')),
                ('realname', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
            ],
        ),
        migrations.AddField(
            model_name='commnent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareapp.Users'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareapp.Users'),
        ),
    ]
