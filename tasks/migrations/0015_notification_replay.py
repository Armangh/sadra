# Generated by Django 2.1.5 on 2019-01-14 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_notification_verb'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='replay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Replay'),
        ),
    ]
