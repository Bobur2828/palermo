from django.db import models
from main.models.base import BaseHeader,BaseTitle


class BlogPGHeader(BaseHeader):
    body1_text_ru  = models.CharField(max_length=122)
    body1_text_en = models.CharField(max_length=122, blank=True, null=True)
    body1_description_ru = models.TextField(blank=True)
    body1_description_en = models.TextField(blank=True, null=True)
    body2_text_ru = models.CharField(max_length=122)
    body2_text_en = models.CharField(max_length=122, blank=True, null=True)
    body2_video = models.FileField(upload_to='blogs/header/', null=True, blank=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'BlogPG header'
        verbose_name_plural = 'BlogPG headers'



class Blog(models.Model):
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    description_ru = models.TextField()
    description_en = models.TextField(null = True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    image1 = models.ImageField(upload_to='blogs/')
    image2 = models.ImageField(upload_to='blogs/',null=True)
    text_ru = models.TextField(blank=True,null=True)
    text_en = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'




class BlogElements(BaseTitle):
    image = models.ImageField(upload_to='blogs/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Blog elements'
        verbose_name_plural = 'Blog elements'


