# Generated by Django 4.2.16 on 2024-11-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_summary_remove_blog_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='Portfolio blog', max_length=200),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Blog', max_length=200),
        ),
    ]
