# Generated by Django 2.2.2 on 2019-06-07 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsapp', '0004_postmodel_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='timestamp',
        ),
    ]