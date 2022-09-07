import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class cohort(models.Model):
    CohortID = models.CharField(
        default=uuid.uuid4, max_length=50, primary_key=True)
    CohortName = models.CharField(max_length=30)
    Admin = models.CharField(max_length=100)


class cohortInfos(models.Model):
    id = models.AutoField(primary_key=True)
    cohort = models.ForeignKey(cohort, on_delete=models.CASCADE)
    Member = models.ForeignKey(User, on_delete=models.CASCADE)
    MemberStatus = models.CharField(max_length=60)

    class Meta:
        unique_together = ('cohort', 'Member',)


class ExamInfo(models.Model):
    examID = models.CharField(
        default=uuid.uuid4, max_length=50, primary_key=True)
    examName = models.CharField(max_length=30)
    cohort = models.ForeignKey(cohort, on_delete=models.CASCADE)
    examType = models.CharField(max_length=20)


class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    examID = models.CharField(max_length=50)

    def __str__(self):
        return self.question
        # return {
        #     "numb": 1,
        #     "question": self.question,
        #     "answer": self.ans,
        #     "options": [
        #         self.op1,
        #         self.op2,
        #         self.op3,
        #         self.op4,
        #
