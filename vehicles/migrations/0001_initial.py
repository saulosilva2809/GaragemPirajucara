# Generated by Django 5.1.4 on 2024-12-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10, unique=True)),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]