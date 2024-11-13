# Generated by Django 5.1.2 on 2024-11-13 15:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_planificacion_fecha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanificacionApoderado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('documento', models.FileField(blank=True, null=True, upload_to='actividades/')),
                ('subido_a', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
