from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Choice, Question


def index(req):
    question_list = Question.objects.order_by('-pub_date')[:5]
    return render(req, 'polls/index.html', {'question_list': question_list})


def ping(req):
    return HttpResponse('PONG')


class IndexView(generic.ListView):
    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question


class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # KeyError is returned when no POST['choice'] exists
        return render(req, 'polls/question_detail.html', {
            'question': question,
            'error': "You did not select a valid answer!"
            }
        )
    else:  # did not except
        selected.votes = F('votes') + 1
        selected.save()
        return HttpResponseRedirect(reverse('polls:results',
                                    args=(question.id,)))
