import uuid

from django.db import models
from django.urls.base import reverse
from cohort.models import cohort, ExamInfo


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_record = models.FileField(upload_to="records")
    language = models.CharField(max_length=50, null=True, blank=True)
    cohort_id = models.ForeignKey(
        cohort,
        related_name="record_cohort_id",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    exam_id = models.ForeignKey(
        ExamInfo,
        related_name="exam_id",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    answer_record = models.FileField(upload_to="answer", blank=True, null=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("core:record_detail", kwargs={"id": str(self.id)})


class RecordAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_record = models.FileField(upload_to="records_answer")
    language = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Record Answer"
        verbose_name_plural = "Records Answer"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("core:record_detail", kwargs={"id": str(self.id)})
