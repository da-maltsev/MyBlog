# Generated by Django 4.1.6 on 2023-02-08 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image_tag_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='image',
        ),
    ]