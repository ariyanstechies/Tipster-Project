# Generated by Django 2.2.4 on 2019-11-06 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191104_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='over15',
            old_name='tip_ov_odds',
            new_name='odds',
        ),
        migrations.RenameField(
            model_name='over15',
            old_name='tip_ov',
            new_name='pick',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='tip_ov_odds',
            new_name='odds',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='tip_ov',
            new_name='pick',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='tip_ov_odds',
            new_name='odds',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='tip_ov',
            new_name='pick',
        ),
    ]
