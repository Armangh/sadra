# Generated by Django 2.1.5 on 2019-01-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20190109_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]