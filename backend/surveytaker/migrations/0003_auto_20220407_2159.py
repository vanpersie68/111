# Generated by Django 3.2.7 on 2022-04-07 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveytaker', '0002_auto_20220407_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='userAction',
            new_name='user_action',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='userAgent',
            new_name='user_agent',
        ),
    ]