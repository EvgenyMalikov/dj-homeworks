# Generated by Django 3.1.2 on 2020-11-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201112_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(through='articles.Scope', to='articles.Article'),
        ),
    ]
