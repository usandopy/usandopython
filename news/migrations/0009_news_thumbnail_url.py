# Generated by Django 3.1.4 on 2021-10-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='thumbnail_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
