# Generated by Django 4.1 on 2022-08-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date", models.DateField(auto_now_add=True)),
                ("discription", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="blog/images")),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
