# Generated by Django 3.2.15 on 2022-08-11 16:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_remove_post_vote_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote_count',
            field=models.ManyToManyField(blank=True, related_name='vote_count', to=settings.AUTH_USER_MODEL),
        ),
    ]