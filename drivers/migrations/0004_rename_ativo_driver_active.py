# Generated by Django 5.1.4 on 2024-12-20 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_remove_driver_status_driver_ativo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='ativo',
            new_name='active',
        ),
    ]
