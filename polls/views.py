from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Question


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    return render(request, 'polls/result.html', {'question': question})