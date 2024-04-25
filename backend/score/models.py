from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    question_category = models.CharField(max_length=30)
    question_context = models.CharField(max_length=500,default="")

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    answer_category = models.CharField(max_length=30)

class Score(models.Model):
    score_value = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')

from score.models import Score  # replace 'your_app_name' with the name of your app
