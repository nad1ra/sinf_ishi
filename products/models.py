from django.db import models
from common.base_models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)


    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='products/')

