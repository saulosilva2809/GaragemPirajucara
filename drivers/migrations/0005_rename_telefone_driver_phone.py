# Generated by Django 5.1.4 on 2024-12-20 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_rename_ativo_driver_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='telefone',
            new_name='phone',
        ),
    ]
