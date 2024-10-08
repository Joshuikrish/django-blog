from django.db import models
from django.utils import timezone
from datetime import datetime


class Question(models.Model):
    
    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    
    def __str__(self) -> str:
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")
    # auto add author
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='blog_images/',null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def summary(self):
        return self.body[:175]+'...'
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
    
    
  
    
