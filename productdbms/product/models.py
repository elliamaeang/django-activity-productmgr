from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator 
from decimal import Decimal

# Create your models here.
class Product(models.Model):

    class CategoryChoices(models.TextChoices):
        ELECTRONICS = 'EL', _('Electronics')
        CLOTHES = 'CL', _('Clothing and Apparel')
        FOOD = 'FO', _('Food')

    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=CategoryChoices.choices)
    price = models.DecimalField("Price (in PHP)", max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name