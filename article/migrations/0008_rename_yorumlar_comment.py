# Generated by Django 4.1.3 on 2022-11-30 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_yorumlar_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Yorumlar',
            new_name='Comment',
        ),
    ]
