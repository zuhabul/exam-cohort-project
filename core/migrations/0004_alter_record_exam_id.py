# Generated by Django 4.1 on 2022-09-06 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cohort", "0001_initial"),
        ("core", "0003_record_exam_id_alter_record_cohort_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="exam_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exam_id",
                to="cohort.examinfo",
            ),
        ),
    ]
