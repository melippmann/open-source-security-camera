# Generated by Django 4.0.3 on 2022-04-10 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recording_file_name_recording_file_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recording',
            old_name='camera_id',
            new_name='cameraId',
        ),
        migrations.RenameField(
            model_name='recording',
            old_name='file_name',
            new_name='fileName',
        ),
        migrations.RenameField(
            model_name='recording',
            old_name='file_path',
            new_name='filePath',
        ),
        migrations.RenameField(
            model_name='recording',
            old_name='recorded_on',
            new_name='recordedOn',
        ),
        migrations.RenameField(
            model_name='recording',
            old_name='recording_length',
            new_name='recordingLength',
        ),
    ]
