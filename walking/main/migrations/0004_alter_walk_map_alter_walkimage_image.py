# Generated by Django 4.0.5 on 2022-06-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_walk_map_alter_walkimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='map',
            field=models.FileField(upload_to='maps/'),
        ),
        migrations.AlterField(
            model_name='walkimage',
            name='image',
            field=models.FileField(upload_to='walks/'),
        ),
    ]
