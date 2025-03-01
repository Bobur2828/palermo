from django.db import models
from main.models.base import BaseHeader,BaseTitle

class ServicePGHeader(BaseHeader):
    body1_text_ru = models.CharField(max_length=222)
    body1_text_en = models.CharField(max_length=222, blank=True, null=True)
    body1_description_en = models.CharField(max_length=255, blank=True, null=True)
    body1_description_ru = models.CharField(max_length=255, blank=True, null=True)

    body2_text_ru = models.CharField(max_length=222)
    body2_text_en = models.CharField(max_length=222, blank=True, null=True)
    body2_description_en = models.CharField(max_length=255, blank=True, null=True)
    body2_description_ru = models.CharField(max_length=255, blank=True, null=True)
    body2_image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'ServicePG Header'
        verbose_name_plural = 'ServicePG Headers'

class Consultations1(BaseTitle):
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Consultations1'
        verbose_name_plural = 'Consultations1'


class Consultations2(BaseTitle):
    image = models.ImageField(upload_to='services/')
    color = models.ImageField(upload_to='services/', null=True)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Consultations2'
        verbose_name_plural = 'Consultations2'


class Consultations3(BaseTitle):
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Consultations3'
        verbose_name_plural = 'Consultations3'

class ServicePGClients(models.Model):
    image = models.ImageField(upload_to='clients/')


    class Meta:
        verbose_name = 'ServicePG Clients'
        verbose_name_plural = 'ServicePG Clients'
