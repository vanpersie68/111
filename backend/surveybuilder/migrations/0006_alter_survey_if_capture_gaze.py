# Generated by Django 3.2.7 on 2022-05-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0005_survey_if_capture_gaze'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='if_capture_gaze',
            field=models.BooleanField(default=False),
        ),
    ]
