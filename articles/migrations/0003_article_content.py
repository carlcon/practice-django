# Generated by Django 3.2.23 on 2023-12-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]