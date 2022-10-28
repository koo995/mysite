from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #질문내용
    pub_date = models.DateTimeField('date published') #생성날짜
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #선택지에 해당하는 질문, 
    #ForeignKey은 Question이라는 데이터 모델을 참조하겠다라는것, Question에서 삭제가 되면 여기서도 삭제가 되도록 하는것
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 투표에 해당
    
    def __str__(self):
        return self.choice_text