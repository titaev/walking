# Generated by Django 4.0.5 on 2022-06-05 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_walk_walkimage_rewiew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiew',
            name='rating',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='walk',
            name='map',
            field=models.FileField(upload_to='media/maps/'),
        ),
        migrations.AlterField(
            model_name='walkimage',
            name='image',
            field=models.FileField(upload_to='media/walks/'),
        ),
    ]
