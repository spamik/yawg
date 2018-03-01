from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    c = {'msg': request.get_host()}
    return HttpResponse(render(request, 'yawg/infomsg.html', c))
