# Generated by Django 2.1 on 2018-08-13 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0015_auto_20180813_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='user',
            new_name='user_id',
        ),
    ]
