# Generated by Django 5.1.3 on 2025-02-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_author_email_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_query_name='tags', to='blog.tag'),
        ),
    ]
