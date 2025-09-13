from django.db import models

# Create your models here.
# questions and published date
class Question(models.Model):
    qustion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
# choices and votes
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)