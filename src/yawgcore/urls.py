from django.urls import path
from django.views.generic import TemplateView

from yawgcore import views

urlpatterns = [
    path('', views.list_gallery),
    path('browse/<path:url>', views.list_gallery),
    path('gadmin/', views.GalleryListView.as_view(), name='yawg-gadmin-index'),
    path('gadmin/gallery/new', views.GalleryCreate.as_view(), name='yawg-gadmin-gallery-new')
]
