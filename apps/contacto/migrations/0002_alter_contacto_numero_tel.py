# Generated by Django 4.2.3 on 2023-07-26 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='numero_tel',
            field=models.CharField(max_length=20),
        ),
    ]
