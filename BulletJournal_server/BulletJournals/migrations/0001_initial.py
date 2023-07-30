# Generated by Django 4.1.10 on 2023-07-28 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('JournalBlueprints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('variant_id', models.AutoField(db_column='BID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('journal_id', models.BigAutoField(db_column='BID', primary_key=True, serialize=False)),
                ('blueprint', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JournalBlueprints.blueprint')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
                ('variant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BulletJournals.variant')),
            ],
        ),
    ]
