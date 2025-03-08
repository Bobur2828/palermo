from django.db import models
from main.models.base import BaseHeader


class HomePG(models.Model):
    title_ru = models.CharField(max_length=255, verbose_name="📌 Заголовок (RU)", blank=True, null=True)
    title_en = models.CharField(max_length=255, verbose_name="📌 Заголовок (EN)", blank=True, null=True)
    image = models.ImageField(upload_to='header/banners/', verbose_name="🖼 Баннер", blank=True, null=True)
    
    description_ru = models.TextField(verbose_name="📝 Описание (RU)", blank=True, null=True)
    description_en = models.TextField(verbose_name="📝 Описание (EN)", blank=True, null=True)
    
    minititle_ru = models.CharField(max_length=255, verbose_name="🔹 Мини-заголовок (RU)", blank=True, null=True)
    minititle_en = models.CharField(max_length=255, verbose_name="🔹 Мини-заголовок (EN)", blank=True, null=True)
    
    color_image_1 = models.ImageField(upload_to='header/color/', verbose_name="🎨 Цветное изображение 1", blank=True, null=True)
    color_image_2 = models.ImageField(upload_to='header/color/', verbose_name="🎨 Цветное изображение 2", blank=True, null=True)

    about_title_ru = models.CharField(max_length=255, verbose_name="ℹ️ Заголовок 'О нас' (RU)", blank=True, null=True)
    about_title_en = models.CharField(max_length=255, verbose_name="ℹ️ Заголовок 'О нас' (EN)", blank=True, null=True)
    
    about_description_ru = models.TextField(verbose_name="📄 Описание 'О нас' (RU)", blank=True, null=True)
    about_description_en = models.TextField(verbose_name="📄 Описание 'О нас' (EN)", blank=True, null=True)

    image1_title_ru = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 1 (RU)", blank=True, null=True)
    image1_title_en = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 1 (EN)", blank=True, null=True)
    image1_description_ru = models.TextField(verbose_name="🖊 Описание изображения 1 (RU)", blank=True, null=True)
    image1_description_en = models.TextField(verbose_name="🖊 Описание изображения 1 (EN)", blank=True, null=True)
    image1 = models.ImageField(upload_to='header/color/', verbose_name="🖼 Изображение 1", blank=True, null=True)

    image2_title_ru = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 2 (RU)", blank=True, null=True)
    image2_title_en = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 2 (EN)", blank=True, null=True)
    image2_description_ru = models.TextField(verbose_name="🖊 Описание изображения 2 (RU)", blank=True, null=True)
    image2_description_en = models.TextField(verbose_name="🖊 Описание изображения 2 (EN)", blank=True, null=True)
    image2 = models.ImageField(upload_to='header/color/', verbose_name="🖼 Изображение 2", blank=True, null=True)

    image3_title_ru = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 3 (RU)", blank=True, null=True)
    image3_title_en = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 3 (EN)", blank=True, null=True)
    image3_description_ru = models.TextField(verbose_name="🖊 Описание изображения 3 (RU)", blank=True, null=True)
    image3_description_en = models.TextField(verbose_name="🖊 Описание изображения 3 (EN)", blank=True, null=True)
    image3 = models.ImageField(upload_to='header/color/', verbose_name="🖼 Изображение 3", blank=True, null=True)

    image4_title_ru = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 4 (RU)", blank=True, null=True)
    image4_title_en = models.CharField(max_length=255, verbose_name="🏞 Заголовок изображения 4 (EN)", blank=True, null=True)
    image4_description_ru = models.TextField(verbose_name="🖊 Описание изображения 4 (RU)", blank=True, null=True)
    image4_description_en = models.TextField(verbose_name="🖊 Описание изображения 4 (EN)", blank=True, null=True)
    image4 = models.ImageField(upload_to='header/color/', verbose_name="🖼 Изображение 4", blank=True, null=True)

    class Meta:
        verbose_name = "🏠 Главная страница"
        verbose_name_plural = "🏠 Главные страницы"

    def __str__(self):
        return self.title_ru if self.title_ru else "Главная страница"











class HomePGAbout(models.Model):
    title_ru = models.CharField(max_length=120, verbose_name="Заголовок (русский)")
    title_en = models.CharField(max_length=120, verbose_name="Заголовок (английский)")
    text_ru = models.TextField(verbose_name="Текст (русский)")
    text_en = models.TextField(verbose_name="Текст (английский)")

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'О нас (главная страница)'
        verbose_name_plural = 'О нас (главная страница)'

class HomePGOffers(models.Model):
    image = models.ImageField(upload_to='offers-images/', verbose_name="Изображение")
    title_ru = models.CharField(max_length=120, verbose_name="Заголовок (русский)")
    title_en = models.CharField(max_length=120, verbose_name="Заголовок (английский)")
    description_ru = models.TextField(verbose_name="Описание (русский)")
    description_en = models.TextField(verbose_name="Описание (английский)")

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Предложение (главная страница)'
        verbose_name_plural = 'Предложения (главная страница)'