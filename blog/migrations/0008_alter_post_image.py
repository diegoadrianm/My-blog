# Generated by Django 5.1.3 on 2025-03-31 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
