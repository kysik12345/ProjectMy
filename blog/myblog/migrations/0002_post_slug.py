# Generated by Django 5.0.7 on 2024-08-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200, unique=True),
        ),
    ]
