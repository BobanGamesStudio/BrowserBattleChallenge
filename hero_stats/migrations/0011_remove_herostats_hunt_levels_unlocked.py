# Generated by Django 4.0.1 on 2024-07-22 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero_stats', '0010_herostats_hunt_levels_unlocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herostats',
            name='hunt_levels_unlocked',
        ),
    ]
