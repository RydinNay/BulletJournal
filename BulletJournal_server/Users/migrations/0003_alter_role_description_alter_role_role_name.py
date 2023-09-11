# Generated by Django 4.1.10 on 2023-08-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_roles_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Role Description'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=20, verbose_name='Role Name'),
        ),
    ]
