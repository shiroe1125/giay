# Generated by Django 4.2.4 on 2023-09-18 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_remove_slide_category_slide_delete_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_sub',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
    ]
