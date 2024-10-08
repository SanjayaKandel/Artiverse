# Generated by Django 5.0.6 on 2024-09-07 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0016_alter_artwork_artist_alter_artwork_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_artist': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='year_created',
            field=models.DateField(null=True),
        ),
    ]
