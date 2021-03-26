from django.db import models


class Project(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.TextField()
    para_1 = models.TextField()
    para_2 = models.TextField(null=True, blank=True)
    para_3 = models.TextField(null=True, blank=True)
    keywords = models.TextField()
    link = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
