from django.db import models
from main.models.base import BaseHeader

class HomePageHeader(BaseHeader):
    text1_ru = models.TextField()
    text1_en = models.TextField()
    text2_ru = models.TextField()
    text2_en = models.TextField()
    color_image_1 = models.ImageField(upload_to='header/color/')
    color_image_2 = models.ImageField(upload_to='header/color/')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'HomePG Header'
        verbose_name_plural = 'HomePG Headers'




class HomePGAbout(models.Model):
    title_ru = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    text_ru = models.TextField()
    text_en = models.TextField()

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'HomePG about'
        verbose_name_plural = 'HomePG about'


class HomePGOffers(models.Model):
    image = models.ImageField(upload_to='offers-images/')
    title_ru = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    description_ru = models.TextField()
    description_en = models.TextField()


    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'HomePG Offer'
        verbose_name_plural = 'HomePG Offers'



