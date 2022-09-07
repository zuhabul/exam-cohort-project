# Generated by Django 4.1 on 2022-09-07 15:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_record_exam_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecordAnswer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("voice_record", models.FileField(upload_to="records_answer")),
                ("language", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Record Answer",
                "verbose_name_plural": "Records Answer",
            },
        ),
    ]
