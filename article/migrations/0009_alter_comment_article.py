# Generated by Django 4.1.3 on 2022-11-30 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_rename_yorumlar_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deli', to='article.article', verbose_name='Makale'),
        ),
    ]
