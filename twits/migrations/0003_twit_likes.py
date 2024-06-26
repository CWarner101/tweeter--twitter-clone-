# Generated by Django 4.0.10 on 2024-04-01 14:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twits', '0002_rename_date_twit_created_twit_updated_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
