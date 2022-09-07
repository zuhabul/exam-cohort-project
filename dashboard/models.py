from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    Question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=80)
    option2 = models.CharField(max_length=80)
    option3 = models.CharField(max_length=80)
    option4 = models.CharField(max_length=80)
    rightAnswer = models.CharField(max_length=80)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    mark = models.IntegerField()