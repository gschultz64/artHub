# Generated by Django 2.1 on 2018-08-10 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_media_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='file',
            field=models.ImageField(default=None, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
