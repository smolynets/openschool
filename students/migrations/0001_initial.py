# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('date', models.DateField(verbose_name='dates', blank=True)),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('notes', models.TextField(verbose_name='Additional notes', blank=True)),
                ('user_g', models.CharField(max_length=256, verbose_name='user')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('user_j', models.CharField(max_length=256, verbose_name='user')),
                ('present_day1', models.CharField(max_length=256, verbose_name='present_day1')),
                ('present_day2', models.CharField(max_length=256, verbose_name='present_day2')),
                ('present_day3', models.CharField(max_length=256, verbose_name='present_day3')),
                ('present_day4', models.CharField(max_length=256, verbose_name='present_day4')),
                ('present_day5', models.CharField(max_length=256, verbose_name='present_day5')),
                ('present_day6', models.CharField(max_length=256, verbose_name='present_day6')),
                ('present_day7', models.CharField(max_length=256, verbose_name='present_day7')),
                ('present_day8', models.CharField(max_length=256, verbose_name='present_day8')),
                ('present_day9', models.CharField(max_length=256, verbose_name='present_day9')),
                ('present_day10', models.CharField(max_length=256, verbose_name='present_day10')),
                ('present_day11', models.CharField(max_length=256, verbose_name='present_day11')),
                ('present_day12', models.CharField(max_length=256, verbose_name='present_day12')),
                ('present_day13', models.CharField(max_length=256, verbose_name='present_day13')),
                ('present_day14', models.CharField(max_length=256, verbose_name='present_day14')),
                ('present_day15', models.CharField(max_length=256, verbose_name='present_day15')),
                ('present_day16', models.CharField(max_length=256, verbose_name='present_day16')),
                ('present_day17', models.CharField(max_length=256, verbose_name='present_day17')),
                ('present_day18', models.CharField(max_length=256, verbose_name='present_day18')),
                ('present_day19', models.CharField(max_length=256, verbose_name='present_day19')),
                ('present_day20', models.CharField(max_length=256, verbose_name='present_day20')),
                ('present_day21', models.CharField(max_length=256, verbose_name='present_day21')),
                ('present_day22', models.CharField(max_length=256, verbose_name='present_day22')),
                ('present_day23', models.CharField(max_length=256, verbose_name='present_day23')),
                ('present_day24', models.CharField(max_length=256, verbose_name='present_day24')),
                ('present_day25', models.CharField(max_length=256, verbose_name='present_day25')),
                ('present_day26', models.CharField(max_length=256, verbose_name='present_day26')),
                ('present_day27', models.CharField(max_length=256, verbose_name='present_day27')),
                ('present_day28', models.CharField(max_length=256, verbose_name='present_day28')),
                ('present_day29', models.CharField(max_length=256, verbose_name='present_day29')),
                ('present_day30', models.CharField(max_length=256, verbose_name='present_day30')),
                ('present_day31', models.CharField(max_length=256, verbose_name='present_day31')),
            ],
            options={
                'verbose_name': 'Monthly journal',
                'verbose_name_plural': 'Monthly journals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=256, verbose_name='last_name')),
                ('birthday', models.DateField(null=True, verbose_name='birthday', blank=True)),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='photo', blank=True)),
                ('ticket', models.CharField(max_length=256, verbose_name='ticket', blank=True)),
                ('notes', models.TextField(verbose_name='Additional notes', blank=True)),
                ('user_s', models.CharField(max_length=256, verbose_name='user')),
                ('student_group_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='group', to='students.Group', null=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(unique_for_month=b'date', verbose_name='Student', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='leader'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(verbose_name='Group', to='students.Group', null=True),
            preserve_default=True,
        ),
    ]
