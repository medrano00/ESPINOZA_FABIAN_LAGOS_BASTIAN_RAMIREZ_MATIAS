# Generated by Django 5.1.2 on 2024-12-05 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_notas_curso_id_alter_notas_estudiante_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notas',
            unique_together={('Estudiante_ID', 'Curso_ID')},
        ),
    ]
