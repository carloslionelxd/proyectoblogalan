# Generated by Django 4.2.3 on 2023-08-03 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_comentario_creator_comentario_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='usuario',
            new_name='creador',
        ),
    ]