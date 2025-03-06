from django.db import models
from main.models.base import BaseHeader, BaseTitle, AutoTranslateMixin


class ServicePGHeader(BaseHeader, AutoTranslateMixin):
    body1_text_ru = models.CharField(max_length=222)
    body1_text_en = models.CharField(max_length=222, blank=True, null=True)
    body1_description_ru = models.CharField(max_length=255, blank=True, null=True)
    body1_description_en = models.CharField(max_length=255, blank=True, null=True)

    body2_text_ru = models.CharField(max_length=222)
    body2_text_en = models.CharField(max_length=222, blank=True, null=True)
    body2_description_ru = models.CharField(max_length=255, blank=True, null=True)
    body2_description_en = models.CharField(max_length=255, blank=True, null=True)
    body2_image = models.ImageField(upload_to='services/')

    translate_fields = {
        'title_ru': 'title_en',
        'title_en': 'title_ru',
        'body1_text_ru': 'body1_text_en',
        'body1_text_en': 'body1_text_ru',
        'body1_description_ru': 'body1_description_en',
        'body1_description_en': 'body1_description_ru',
        'body2_text_ru': 'body2_text_en',
        'body2_text_en': 'body2_text_ru',
        'body2_description_ru': 'body2_description_en',
        'body2_description_en': 'body2_description_ru',

    }

    def save(self, *args, **kwargs):
        self.auto_translate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'ServicePG Header'
        verbose_name_plural = 'ServicePG Headers'


class Consultations1(BaseTitle, AutoTranslateMixin):
    image = models.ImageField(upload_to='services/')
    translate_fields = {
        'title_ru': 'title_en',
        'title_en': 'title_ru',
        'description_ru': 'description_en',
        'description_en': 'description_ru',
    }

    def save(self, *args, **kwargs):
        self.auto_translate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Consultations1'
        verbose_name_plural = 'Consultations1'


class Consultations2(BaseTitle, AutoTranslateMixin):
    image = models.ImageField(upload_to='services/')
    color = models.ImageField(upload_to='services/', null=True)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    translate_fields = {
        'title_ru': 'title_en',
        'title_en': 'title_ru',
        'description_ru': 'description_en',
        'description_en': 'description_ru',
        'text_ru': 'text_en',
        'text_en': 'text_ru',
    }

    def save(self, *args, **kwargs):
        self.auto_translate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Consultations2'
        verbose_name_plural = 'Consultations2'


class Consultations3(BaseTitle, AutoTranslateMixin):
    image = models.ImageField(upload_to='services/')
    translate_fields = {
        'title_ru': 'title_en',
        'title_en': 'title_ru',
        'description_ru': 'description_en',
        'description_en': 'description_ru',
    }

    def save(self, *args, **kwargs):
        self.auto_translate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Consultations3'
        verbose_name_plural = 'Consultations3'


class ServicePGClientsTitle(models.Model, AutoTranslateMixin):
    number = models.CharField(max_length=23)
    text_ru = models.CharField(max_length=122, blank=True, null=True)
    text_en = models.CharField(max_length=122, blank=True, null=True)
    translate_fields = {
        'text_ru': 'text_en',
        'text_en': 'text_ru',
    }

    def save(self, *args, **kwargs):
        self.auto_translate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'ServicePG ClientsTitle'
        verbose_name_plural = 'ServicePG ClientsTitles'


class ServicePGClients(models.Model):
    image = models.ImageField(upload_to='clients/')

    class Meta:
        verbose_name = 'ServicePG Clients'
        verbose_name_plural = 'ServicePG Clients'
