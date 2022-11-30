# Generated by Django 4.1.3 on 2022-11-29 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_rename_media_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yorumlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorumcu_adı', models.CharField(max_length=20, verbose_name='İsim')),
                ('yorumcu_yorumu', models.CharField(max_length=20, verbose_name='Yorum')),
                ('yorumcu_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='article.article', verbose_name='Makale')),
            ],
        ),
    ]
