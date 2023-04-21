from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    course = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)
    
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    teaching = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)
