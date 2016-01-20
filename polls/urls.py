from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    # polls
    url(r'^$', views.index, name='index'),

    # polls/ping
    url(r'ping/$', views.ping, name='ping'),

    # polls/5
    # (?P<foo>) is a capturing group named foo
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # polls/5/result
    url(r'^(?P<question_id>[0-9]+)/result$', views.result, name='result'),

    # polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote')
]
