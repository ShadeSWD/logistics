from django.db import models
from config import settings

NULLABLE = {"null": True, "blank": True}


class Contacts(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    email = models.EmailField(verbose_name='email')
    country = models.CharField(verbose_name='country', max_length=60)
    city = models.CharField(verbose_name='city', max_length=100)
    street = models.CharField(verbose_name='street', max_length=100)
    house = models.IntegerField(verbose_name='house number')
    building = models.IntegerField(verbose_name='building number', **NULLABLE)
    letter = models.CharField(verbose_name='building letter', max_length=5)

    class Meta:
        verbose_name = 'contacts'
        verbose_name_plural = 'contacts'


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    name = models.CharField(verbose_name='name', max_length=100)
    model = models.CharField(verbose_name='model', max_length=100)
    release_date = models.DateField(verbose_name='release date')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Dealer(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    name = models.CharField(verbose_name='name', max_length=100)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'dealer'
        verbose_name_plural = 'dealers'
