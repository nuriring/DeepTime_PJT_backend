# Generated by Django 3.2.12 on 2022-05-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OTT',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_id', models.IntegerField()),
                ('provider_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('backdrop_path', models.TextField()),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('release_date', models.DateField()),
                ('vote_average', models.FloatField()),
                ('poster_path', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('genre', models.ManyToManyField(related_name='movie_genre', to='movies.Genre')),
            ],
        ),
    ]
