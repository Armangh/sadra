# Generated by Django 2.1.5 on 2019-01-12 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_auto_20190110_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replay',
            name='employee',
        ),
        migrations.AddField(
            model_name='replay',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
