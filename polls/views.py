from django.http import HttpResponse


def index(req):
    return HttpResponse('Hello world, you are at the polls index.')


def ping(req):
    return HttpResponse('PONG')
