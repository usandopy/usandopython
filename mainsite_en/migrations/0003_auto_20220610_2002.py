# Generated by Django 2.2.16 on 2022-06-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite_en', '0002_auto_20220610_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='editor_choice',
            new_name='editor_choice_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='hot_news',
            new_name='hot_news_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_five',
            new_name='post_catalog_five_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_four',
            new_name='post_catalog_four_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_one',
            new_name='post_catalog_one_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_three',
            new_name='post_catalog_three_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_two',
            new_name='post_catalog_two_en',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='trending',
            new_name='trending_en',
        ),
    ]
