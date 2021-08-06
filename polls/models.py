from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone
from django.shortcuts import render


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

def index(request):
    question_list = Question.objects.all().filter(
        pub_date__lte=timezone.now()
    )
    context = {'question_list': question_list}

    return render(request, 'polls/index.html', context)

def index(request):
    question_list = Question.objects.all().filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {'question_list': question_list}

    return render(request, 'polls/index.html', context)