from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView

from yawgcore.forms import GalleryForm
from yawgcore.models import GalleryDomainMap, Gallery


def list_gallery(request, url=None):
    try:
        GalleryDomainMap.objects.get(domain_host=request.get_host())
    except GalleryDomainMap.DoesNotExist:
        # this domain has no associated gallery
        c = {'msg': 'No gallery defined at site %s' % request.get_host()}
        return HttpResponse(render(request, 'yawg/infomsg.html', c))
    c = {'msg': 'blabla'}
    return HttpResponse(render(request, 'yawg/infomsg.html', c))


class GalleryListView(ListView):
    template_name = 'yawg/gadmin/gallery_list.html'

    def get_queryset(self):
        return Gallery.objects.all().order_by('gallery_name')


class GalleryCreate(CreateView):
    template_name = 'yawg/gadmin/gallery_edit.html'
    model = Gallery
    fields = ['gallery_name', 'gallery_alias']

