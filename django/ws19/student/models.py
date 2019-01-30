from django.db import models

# Create your models here.
class Student(models.Model): # Model명은 보통 단수로 작성
    name = models.CharField(max_length=100) # CharField에는 반드시 max_length 필요
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
