# Generated by Django 3.1.1 on 2024-08-16 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pushsubscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pushsubscription',
            name='subscription_info',
        ),
        migrations.AddField(
            model_name='pushsubscription',
            name='auth',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pushsubscription',
            name='endpoint',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='pushsubscription',
            name='p256dh',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pushsubscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
