from django.db import models


class GalleryStorage(models.Model):
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=256)


class Gallery(models.Model):
    gallery_name = models.CharField(max_length=128)
    gallery_alias = models.CharField(max_length=64)


class GalleryDomainMap(models.Model):
    domain_host = models.CharField(max_length=128)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
