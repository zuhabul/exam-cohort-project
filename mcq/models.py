import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class questionModel(models.Model):
    examID = models.CharField(default=uuid.uuid4, max_length=50)
    CohortID = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


    