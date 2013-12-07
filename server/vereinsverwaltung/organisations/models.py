from django.db import models

class Organisation(models.Model):
	name = models.CharField('name', max_length=30, blank=False)
	ngo_number = models.CharField('ngo number', max_length=30, blank=False)
	street = models.CharField('street', max_length=30, blank=False)
	city = models.CharField('city', max_length=30, blank=False)
	postal_code = models.PositiveIntegerField('postal code', max_length=30, blank=False)
	country = models.CharField('country', max_length=30, blank=False)

	