# Generated by Django 4.1.10 on 2023-08-30 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BulletJournals', '0005_alter_journal_termins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='termins',
            field=models.DateField(default=datetime.date(2023, 9, 2)),
        ),
    ]
