from django.test import TestCase
from cars.models import Car

class CarTestCase(TestCase):
	def setUp(self):
		Car.objects.create(name="Ford", plate="1234")
		Car.objects.create(name="Chevrolet", plate="4321")

	def test_car_names(self):
		"""Car names from a plate"""
		ford = Car.objects.get(plate="1234")
		chevrolet = Car.objects.get(plate="4321")
		self.assertEqual(ford.name, 'Ford')
		self.assertEqual(chevrolet.name, 'Chevrolet')