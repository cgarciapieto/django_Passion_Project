# Generated by Django 2.2.2 on 2019-06-07 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsapp', '0002_auto_20190607_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='textField',
            new_name='content',
        ),
    ]
