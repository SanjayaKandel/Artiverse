# Generated by Django 5.0.6 on 2024-09-08 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0019_exhibition_brief_description_exhibition_curator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 9, 8, 14, 34, 39, 768484)),
            preserve_default=False,
        ),
    ]
