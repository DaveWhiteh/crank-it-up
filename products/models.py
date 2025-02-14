from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand_name = models.CharField(max_length=254)
    model_name = models.CharField(max_length=254)
    description = models.TextField()
    size = models.CharField(max_length=254)
    colour = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.model_name
