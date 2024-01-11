from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    gender = models.BooleanField(default=True)
    
    def __str__(self):
        return 'hi' + self.name
class Voter(models.Model):
    id_number=models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    city= models.CharField(max_length=200)
    region= models.CharField(max_length=200)
    def __str__(self):
        return 'hi' + self.first_name
