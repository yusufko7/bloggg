# Generated by Django 4.1.3 on 2022-11-29 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='media',
            new_name='image',
        ),
    ]