# Generated by Django 3.1.3 on 2020-11-20 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registr',
            old_name='password',
            new_name='address',
        ),
    ]
