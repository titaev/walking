# Generated by Django 4.0.5 on 2022-06-05 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('description', models.TextField()),
                ('map', models.FileField(upload_to='maps/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
            ],
        ),
        migrations.CreateModel(
            name='WalkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='walks/')),
                ('walk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.walk')),
            ],
        ),
        migrations.CreateModel(
            name='Rewiew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('walk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.walk')),
            ],
        ),
    ]
