# Generated by Django 2.2.16 on 2022-06-10 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite_en', '0003_auto_20220610_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='editor_choice_en',
            new_name='editor_choice',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='hot_news_en',
            new_name='hot_news',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_five_en',
            new_name='post_catalog_five',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_four_en',
            new_name='post_catalog_four',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_one_en',
            new_name='post_catalog_one',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_three_en',
            new_name='post_catalog_three',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='post_catalog_two_en',
            new_name='post_catalog_two',
        ),
        migrations.RenameField(
            model_name='homepagesettings',
            old_name='trending_en',
            new_name='trending',
        ),
    ]
