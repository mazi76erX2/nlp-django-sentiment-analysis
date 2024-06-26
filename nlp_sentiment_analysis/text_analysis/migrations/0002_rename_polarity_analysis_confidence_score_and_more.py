# Generated by Django 5.0.6 on 2024-05-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("text_analysis", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="analysis",
            old_name="polarity",
            new_name="confidence_score",
        ),
        migrations.RemoveField(
            model_name="analysis",
            name="subjectivity",
        ),
        migrations.AddField(
            model_name="analysis",
            name="sentiment",
            field=models.CharField(
                blank=True,
                choices=[
                    ("positive", "Positive"),
                    ("negative", "Negative"),
                    ("neutral", "Neutral"),
                ],
                max_length=8,
                null=True,
            ),
        ),
    ]
