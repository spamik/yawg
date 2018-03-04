from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView

from yawgcore.forms import GalleryForm
from yawgcore.models import GalleryDomainMap, Gallery


def list_gallery(request, url=None):
    """
    List content of gallery/album
    """
    try:
        GalleryDomainMap.objects.get(domain_host=request.get_host())
    except GalleryDomainMap.DoesNotExist:
        # this domain has no associated gallery
        c = {'msg': 'No gallery defined at site %s' % request.get_host()}
        return HttpResponse(render(request, 'yawg/infomsg.html', c))
    c = {'msg': 'blabla'}
    return HttpResponse(render(request, 'yawg/infomsg.html', c))


class GalleryListView(ListView):
    """
    Admin site - list defined galleries
    """
    template_name = 'yawg/gadmin/gallery_list.html'

    def get_queryset(self):
        return Gallery.objects.all().order_by('gallery_name')


class GalleryCreate(CreateView):
    """
    Create new Gallery (model)
    """
    template_name = 'yawg/gadmin/gallery_edit.html'
    model = Gallery
    fields = ['gallery_name', 'gallery_alias']


class GallerySettings(TemplateView):
    """
    Show settings for gallery
    """
    template_name = 'yawg/gadmin/gallery_settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.get(id=self.kwargs['pk'])
        context['domains'] = GalleryDomainMap.objects.filter(gallery=context['gallery'])
        return context


class GalleryDomainMapCreate(CreateView):
    """
    Creating new domain for gallery
    """
    template_name = 'yawg/gadmin/gallery_domain_edit.html'
    model = GalleryDomainMap
    fields = ('domain_host',)

    def form_valid(self, form):
        """
        fill gallery FK to that passed in URL
        """
        form.instance.gallery = Gallery.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

