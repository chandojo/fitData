# Generated by Django 2.2.4 on 2019-08-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seasonplanduration',
            old_name='season_duration',
            new_name='season_duration_months',
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(help_text='Sport, PostRehab, Quality of Life, etc', max_length=255),
        ),
        migrations.AlterField(
            model_name='workouttype',
            name='name',
            field=models.CharField(help_text='Cardio, Met Con, Strength, Power, etc', max_length=255),
        ),
    ]
