# Generated by Django 4.0.1 on 2024-07-15 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero_stats', '0008_herostats_prev_level_expirience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='herostats',
            old_name='current_expirience',
            new_name='current_experience',
        ),
        migrations.RenameField(
            model_name='herostats',
            old_name='next_level_expirience',
            new_name='next_level_experience',
        ),
        migrations.RenameField(
            model_name='herostats',
            old_name='prev_level_expirience',
            new_name='prev_level_experience',
        ),
    ]
