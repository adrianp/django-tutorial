from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(req):
    question_list = Question.objects.order_by('-pub_date')[:5]
    return render(req, 'polls/index.html', {'question_list': question_list})


def ping(req):
    return HttpResponse('PONG')


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def result(req, question_id):
    return HttpResponse('You are looking at the results of question %s' %
                        question_id)


def vote(req, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)
