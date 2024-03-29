from django.db import models
from config import settings

NULLABLE = {"null": True, "blank": True}


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

    def __str__(self):
        return f'{self.name}'


class Dealer(models.Model):
    FACTORY = 'fac'
    RETAIL = 'ret'
    INDIVIDUAL = 'ind'
    DEALER_TYPES = (
        (FACTORY, 'factory'),
        (RETAIL, 'retail network'),
        (INDIVIDUAL, 'individual entrepreneur'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    name = models.CharField(verbose_name='name', max_length=100)
    dealer_type = models.CharField(verbose_name='dealer type', max_length=3, choices=DEALER_TYPES)
    email = models.EmailField(verbose_name='email')
    country = models.CharField(verbose_name='country', max_length=60)
    city = models.CharField(verbose_name='city', max_length=100)
    street = models.CharField(verbose_name='street', max_length=100)
    house = models.IntegerField(verbose_name='house number')
    building = models.IntegerField(verbose_name='building number', **NULLABLE)
    letter = models.CharField(verbose_name='building letter', max_length=5, **NULLABLE)
    products = models.ManyToManyField(Product, verbose_name='products')
    contractor = models.ForeignKey('Dealer', on_delete=models.PROTECT, **NULLABLE, verbose_name='contractor')
    debt = models.DecimalField(verbose_name='debt', max_digits=20, decimal_places=3, default=0)

    class Meta:
        verbose_name = 'dealer'
        verbose_name_plural = 'dealers'

    def __str__(self):
        return f'{self.name}'

    @property
    def level(self):
        if not self.contractor:
            return 0
        else:
            for dealer in Dealer.objects.all():
                if dealer.contractor:
                    if dealer.contractor.pk == self.pk:
                        return 1
        return 2
