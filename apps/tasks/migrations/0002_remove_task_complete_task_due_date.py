# Generated by Django 4.2.7 on 2023-12-22 08:21

import apps.tasks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=apps.tasks.models.one_week_hence),
        ),
    ]
