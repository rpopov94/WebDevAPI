from django.db import models


class DataMap(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    address = models.CharField(max_length=100, blank=True, default='')
    geoinfo = models.CharField(max_length=100, blank=True, default='')
    parks = models.IntegerField(default=0)
    stores = models.IntegerField(default=0)
    shools = models.IntegerField(default=0)
    kindergartens = models.IntegerField(default=0)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ['id']

