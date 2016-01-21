from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    # polls
    url(r'^$', views.IndexView.as_view(), name='index'),

    # polls/ping
    url(r'ping/$', views.ping, name='ping'),

    # polls/5
    # (?P<foo>) is a capturing group named foo
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # polls/5/result
    url(r'^(?P<pk>[0-9]+)/results$', views.ResultsView.as_view(), 
        name='results'),

    # polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote')
]
