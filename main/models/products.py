from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Products Category'


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=155)
    name_en = models.CharField(max_length=155, null=True, blank=True)
    body_ru = models.TextField()
    body_en = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)  # +
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='products/main_image/')
    image1 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True, auto_now_add=True)
    status = models.IntegerField(
        choices=(
            (1, 'No Faol'),
            (2, "Yo'lda"),
            (3, 'Qaytarilgan'),
            (4, 'Qabul qilingan')
        ),
        default=1
    )


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    count  = models.IntegerField()

    def __str__(self):
        return f'{self.cart.user.username} | {self.product.name_ru}'




class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        obj = WishList.objects.filter(user=self.user, product=self.product)
        if obj.count():
            raise ValueError('Ma`lumot bor')
        super(WishList, self).save(*args, **kwargs)