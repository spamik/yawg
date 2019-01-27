from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class GalleryStorage(models.Model):
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=256)


class ItemMapping(models.Model):
    parent_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='mapping_parent')
    parent_id = models.PositiveIntegerField()
    parent_object = GenericForeignKey('parent_ct', 'parent_id')
    item_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='mapping_item')
    item_id = models.PositiveIntegerField()
    item_object = GenericForeignKey('item_ct', 'item_id')


class Gallery(models.Model):
    gallery_name = models.CharField(max_length=128)
    gallery_alias = models.CharField(max_length=64, unique=True)
    items = GenericRelation(ItemMapping, content_type_field='parent_ct', object_id_field='parent_id')


class GalleryDomainMap(models.Model):
    domain_host = models.CharField(max_length=128, unique=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class Album(models.Model):
    album_name = models.CharField(max_length=128)
    album_alias = models.CharField(max_length=64)
    items = GenericRelation(ItemMapping, content_type_field='parent_ct', object_id_field='parent_id')

    def gallery_name(self):
        return self.album_name

    def browse_url(self):
        return reverse('yawg-list-album', args=([self.id, self.album_alias]))


class GalleryItem(models.Model):
    item_name = models.CharField(max_length=128)
    filename = models.CharField(max_length=64)

    def gallery_name(self):
        return self.item_name

    def browse_url(self):
        return reverse('yawg-list-item', args=([self.id, self.filename]))

