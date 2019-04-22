# Generated by Django 2.1.7 on 2019-04-22 23:02

import django.core.validators
from django.db import migrations, models

import games_launcher.apps.games.storage


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0003_auto_20190409_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='file',
            field=models.FileField(max_length=255, null=True, storage=games_launcher.apps.games.storage.GameStorage(),
                                   upload_to=games_launcher.apps.games.storage.upload_file_to, validators=[
                    django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])]),
        ),
        migrations.AlterField(
            model_name='game',
            name='logo',
            field=models.ImageField(null=True, storage=games_launcher.apps.games.storage.GameStorage(),
                                    upload_to=games_launcher.apps.games.storage.upload_file_to),
        ),
    ]
