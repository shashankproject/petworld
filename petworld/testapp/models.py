from django.db import models

# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=100);
    feedback=models.CharField(max_length=300);
