# Generated by Django 2.2.4 on 2019-08-23 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_auto_20190823_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seasonplanduration',
            old_name='season_duration_months',
            new_name='months',
        ),
    ]
