# Generated by Django 4.0.5 on 2022-06-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_walk_walkimage_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='name',
            field=models.CharField(default='name', max_length=300),
            preserve_default=False,
        ),
    ]
