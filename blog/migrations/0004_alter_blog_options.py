# Generated by Django 4.0.4 on 2022-08-23 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_image_remove_blog_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date'], 'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
    ]
