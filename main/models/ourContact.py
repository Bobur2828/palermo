from django.db import models

class OurSocial(models.Model):
    """Ijtimoiy tarmoqlar"""
    icon = models.ImageField(upload_to='social/')
    link = models.CharField(max_length=120)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Our Social"
        verbose_name_plural = "Our Socials"

    def __str__(self):
        return self.name

class OurData(models.Model):
    """Kontankt sahifasidagi kompaniya malumotlari"""
    contact_title_ru = models.CharField(max_length=100)
    contact_title_en = models.CharField(max_length=100, null=True, blank=True)
    contact_description_ru = models.CharField(max_length=255, null=True, blank=True)
    contact_description_en = models.CharField(max_length=255, null=True, blank=True)

    address_ru = models.CharField(max_length=150)
    address_en = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    latitude = models.PositiveIntegerField(null=True, blank=True)
    longitude = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Our Contact"
        verbose_name_plural = "Our Contacts"
    
    def __str__(self):
        return self.contact_title_ru

class Contacts(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"