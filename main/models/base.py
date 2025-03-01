from django.db import models


class BaseTitle(models.Model):
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class BaseHeader(models.Model):
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='header/banners/')

    class Meta:
        abstract = True
