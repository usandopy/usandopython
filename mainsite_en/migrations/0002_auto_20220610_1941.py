# Generated by Django 2.2.16 on 2022-06-10 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news_en', '0001_initial'),
        ('mainsite_en', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesettings',
            name='editor_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor_choice_en', to='news_en.News'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='hot_news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hot_news_en', to='news_en.News'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='post_catalog_five',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_five_en', to='news_en.Category'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='post_catalog_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_four_en', to='news_en.Category'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='post_catalog_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_one_en', to='news_en.Category'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='post_catalog_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_three_en', to='news_en.Category'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='post_catalog_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_two_en', to='news_en.Category'),
        ),
        migrations.AddField(
            model_name='homepagesettings',
            name='trending',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trending_en', to='news_en.News'),
        ),
    ]