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



from deep_translator import GoogleTranslator

class AutoTranslateMixin:
    """
    Bu mixin har qanday modeldagi tarjima maydonlarini avtomatik tarjima qilishga moslashadi.
    """

    translate_fields = {}  # Modelda qaysi maydonlarni tarjima qilish kerakligini belgilash

    def translate_field(self, field_from, field_to, source_lang, target_lang):
        if hasattr(self, field_from) and hasattr(self, field_to):
            field_from_value = getattr(self, field_from)
            field_to_value = getattr(self, field_to)

            if field_from_value and not field_to_value:  # Agar tarjima kerak bo‘lsa
                translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(field_from_value)
                setattr(self, field_to, translated_text)
                # print(f"✅ Tarjima qilingan: {field_from} -> {field_to}: {translated_text}")  # Debug uchun

    def auto_translate(self):
        for lang_from, lang_to in self.translate_fields.items():
            self.translate_field(lang_from, lang_to, lang_from.split("_")[-1], lang_to.split("_")[-1])

    def save(self, *args, **kwargs):
        self.auto_translate()
        print("💾 Saqlanmoqda...")  # Debug uchun
        super().save(*args, **kwargs)
