from django.db import models

class Car(models.Model):
	name = models.CharField("Car Name", max_length=255)
	plate = models.CharField("Car Plate", max_length=50)

	class Meta:
		db_table = 'car'
		unique_together = ['name', 'plate']
		verbose_name = "Car"
		verbose_name_plural = "Cars"