# Generated by Django 3.1.1 on 2020-10-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='file_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
