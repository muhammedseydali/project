# Generated by Django 3.1.3 on 2020-11-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_final'),
    ]

    operations = [
        migrations.DeleteModel(
            name='final',
        ),
        migrations.AddField(
            model_name='registr',
            name='activate',
            field=models.BooleanField(default=0),
        ),
    ]