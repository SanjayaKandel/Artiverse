# Generated by Django 5.0.6 on 2024-07-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_artist_social_links_delete_sociallink'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='ward_no',
            field=models.IntegerField(null=True),
        ),
    ]
