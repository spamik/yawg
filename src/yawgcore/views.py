from django.http import HttpResponse
from django.shortcuts import render
from yawgcore.models import GalleryDomainMap


def list_gallery(request, url=None):
    try:
        GalleryDomainMap.objects.get(domain_host=request.get_host())
    except GalleryDomainMap.DoesNotExist:
        # this domain has no associated gallery
        c = {'msg': 'No gallery defined at site %s' % request.get_host()}
        return HttpResponse(render(request, 'yawg/infomsg.html', c))
    c = {'msg': 'blabla'}
    return HttpResponse(render(request, 'yawg/infomsg.html', c))
