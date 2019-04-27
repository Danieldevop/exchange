from django.db import models


class ContactForm(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	message = models.TextField()

	def __str__(self):
		return self.name

class ExchangeForm(models.Model):
	amount_to_exchange = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	calculated_value = models.CharField(max_length=15, default='', blank=True, null=True)

