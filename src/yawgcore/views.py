from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    c = {}
    c['host'] = request.get_host()
    return HttpResponse(render(request, 'yawg/layout.html', c))
