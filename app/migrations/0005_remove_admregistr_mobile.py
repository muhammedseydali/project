# Generated by Django 3.1.3 on 2020-11-20 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_admregistr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admregistr',
            name='mobile',
        ),
    ]
