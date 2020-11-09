# Generated by Django 2.2.10 on 2020-10-25 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tags', to='articles.Article'),
        ),
    ]