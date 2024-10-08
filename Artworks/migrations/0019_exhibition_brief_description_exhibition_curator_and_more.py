# Generated by Django 5.0.6 on 2024-09-07 19:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0018_exhibition'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='brief_description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='curator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='exhibitions/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='artworks',
            field=models.ManyToManyField(blank=True, null=True, related_name='exhibitions', to='Artworks.artwork'),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
