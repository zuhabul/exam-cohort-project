from uuid import uuid4
from django.db import models

# Create your models here.

class testing(models.Model):
    id = models.CharField(default = uuid4, primary_key = True, max_length=50)
    text = models.CharField(max_length=50)

