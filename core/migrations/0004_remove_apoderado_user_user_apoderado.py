# Generated by Django 5.1 on 2024-10-03 03:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_apoderado_niño'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apoderado',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='apoderado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.apoderado'),
        ),
    ]
