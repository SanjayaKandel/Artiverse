# Generated by Django 5.0.6 on 2024-07-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_visitor_birth_date_visitor_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='biography',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
