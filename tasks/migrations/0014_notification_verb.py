# Generated by Django 2.1.5 on 2019-01-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='verb',
            field=models.CharField(default='create', max_length=6),
            preserve_default=False,
        ),
    ]
