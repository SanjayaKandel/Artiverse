# Generated by Django 5.0.6 on 2024-07-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0008_artist_age_artist_country_artist_street_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='contact_email',
        ),
        migrations.AlterField(
            model_name='artist',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='contact_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='artist_profiles/'),
        ),
    ]
