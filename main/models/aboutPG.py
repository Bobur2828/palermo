from django.db import models
from main.models.base import BaseHeader,BaseTitle

class AboutPGHeader(BaseHeader):
    description_ru = models.TextField()
    description_en = models.TextField(null=True, blank=True)
    description_color = models.ImageField(upload_to='colors/', null=True, blank=True)
    color1 = models.ImageField(upload_to='colors/', null=True, blank=True)
    color2 = models.ImageField(upload_to='colors/', null=True, blank=True)
    color3 = models.ImageField(upload_to='colors/', null=True, blank=True)

    class Meta:
        verbose_name = 'AboutPG Header'
        verbose_name_plural = 'AboutPG Headers'



    def __str__(self):
        return self.title_ru


class OurWorksTitle(BaseTitle):
    class Meta:
        verbose_name = 'Our Works Title'
        verbose_name_plural = 'Our Works Titles'

    def __str__(self):
        return self.title_ru


class OurWorks(models.Model):
    image = models.ImageField(upload_to='works/')
    name = models.CharField(max_length=122, null=True, blank=True) #xar exitmolga qarshi
    
    class Meta:
        verbose_name = 'Our Works'
        verbose_name_plural = 'Our Works'
    



class AboutPGBlog(BaseTitle):
    image = models.ImageField(upload_to='about/images/')

    class Meta:
        verbose_name = 'AboutPG Blog'
        verbose_name_plural = 'AboutPG Blogs'

    def __str__(self):
        return self.title_ru


class Testimonial(models.Model):
    name = models.CharField(max_length=122, null=True, blank=True)
    avatar = models.ImageField(upload_to='testimonials/avatar/')
    text = models.TextField()
    marks = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='testimonials/')
    image2 = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    image3 = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    image4 = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


    def __str__(self):
        return self.name


