from django.db import models


class Testimonial(models.Model):
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    review = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
