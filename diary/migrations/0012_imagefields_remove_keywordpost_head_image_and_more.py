# Generated by Django 4.1.2 on 2022-11-14 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0011_alter_keywordpost_drawing_alter_keywordpost_emotion_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageFields",
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
                ("mainImage", models.ImageField(upload_to="")),
                ("keywords", models.TextField()),
                ("url1", models.TextField()),
                ("url2", models.TextField()),
                ("url3", models.TextField()),
                ("url4", models.TextField()),
            ],
        ),
        migrations.RemoveField(model_name="keywordpost", name="head_image",),
        migrations.RemoveField(model_name="memory", name="head_image",),
        migrations.AlterField(
            model_name="keywordpost",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("Sketched", "Sketched"),
                    ("Digital Art", "Digital Art"),
                    ("Impressionism", "Impressionism"),
                    ("Oil and Canvas", "Oil and Canvas"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="Emotion",
            field=models.CharField(
                choices=[
                    ("Angry", "Angry"),
                    ("Depressed", "Depressed"),
                    ("Neutral", "Neutral"),
                    ("Happy", "Happy"),
                    ("Cheerful", "Cheerful"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="Weather",
            field=models.CharField(
                choices=[
                    ("Rainy", "Rainy"),
                    ("Cloudy", "Cloudy"),
                    ("Snowy", "Snowy"),
                    ("Sunny", "Sunny"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("Sketched", "Sketched"),
                    ("Digital Art", "Digital Art"),
                    ("Impressionism", "Impressionism"),
                    ("Oil and Canvas", "Oil and Canvas"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Emotion",
            field=models.CharField(
                choices=[
                    ("Angry", "Angry"),
                    ("Depressed", "Depressed"),
                    ("Neutral", "Neutral"),
                    ("Happy", "Happy"),
                    ("Cheerful", "Cheerful"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Weather",
            field=models.CharField(
                choices=[
                    ("Rainy", "Rainy"),
                    ("Cloudy", "Cloudy"),
                    ("Snowy", "Snowy"),
                    ("Sunny", "Sunny"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]