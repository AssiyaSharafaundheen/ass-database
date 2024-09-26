from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField (max_length=60)
    phone=models.IntegerField()

    def __str__(self):
        return  self.name