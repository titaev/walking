# Generated by Django 4.0.5 on 2022-06-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rewiew_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiew',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
