# Generated by Django 3.2.23 on 2024-03-24 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filtaer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_filtaer',
            new_name='image_filter',
        ),
    ]
