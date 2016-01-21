from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question


def index(req):
    question_list = Question.objects.order_by('-pub_date')[:5]
    return render(req, 'polls/index.html', {'question_list': question_list})


def ping(req):
    return HttpResponse('PONG')


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_id):
    return render(req, 'polls/results.html',
                  {'question': get_object_or_404(Question, pk=question_id)})


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # KeyError is returned when no POST['choice'] exists
        return render(req, 'polls/detail.html', {
            'question': question,
            'error': "You did not select a valid answer!"
            }
        )
    else:  # did not except
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse('polls:results',
                                    args=(question.id,)))
