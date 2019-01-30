from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
# Question : Choice = 1 : N    
class Choice(models.Model):
    quetion = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    votes = models.IntegerField()