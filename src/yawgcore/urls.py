from django.urls import path
from django.views.generic import TemplateView

from yawgcore import views

urlpatterns = [
    path('', views.list_gallery),
    path('browse/<int:album>/<str:alias>/', views.list_gallery, name='yawg-list-album'),
    path('view-item/<int:item>/<str:filename>/', views.list_item, name='yawg-list-item'),
    path('gadmin/', views.GalleryListView.as_view(), name='yawg-gadmin-index'),
    path('gadmin/gallery/new', views.GalleryCreate.as_view(), name='yawg-gadmin-gallery-new'),
    path('gadmin/gallery/<int:pk>/settings', views.GallerySettings.as_view(), name='yawg-gadmin-gallery-settings'),
    path('gadmin/gallery/<int:pk>/domain/new', views.GalleryDomainMapCreate.as_view(),
         name='yawg-gadmin-gallery-domain-new'),
]
