# Generated by Django 4.0 on 2022-10-16 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.movie'),
        ),
    ]
