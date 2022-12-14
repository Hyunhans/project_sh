# Generated by Django 4.1.2 on 2022-11-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0009_alter_keywordpost_drawing_alter_keywordpost_emotion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keywordpost",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("Sketched", "Sketched"),
                    ("Digital Art", "Digital Art"),
                    ("Oil and Canvas", "Oil and Canvas"),
                    ("Impressionism", "Impressionism"),
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
                    ("Oil and Canvas", "Oil and Canvas"),
                    ("Impressionism", "Impressionism"),
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
