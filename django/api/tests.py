from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Car
import json

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

class APITest(TestCase):
	def setUp(self):
		self.client = APIClient()
		Car.objects.create(name="Ford", plate="1234")

	def test_get_car_name(self):
		"""
			Check that response from API returns a 200 and the correct car name
		"""
		request = self.client.get('/api/1234/')
		self.assertEqual(request.status_code, 200)
		self.assertIs("name" in request.json(), True)
		self.assertEqual(request.json()["name"], "Ford")
	
	def test_get_car_name_wrong(self):		
		"""
			Check that response from API returns a 404 and the "name" key is not in the response
		"""
		request = self.client.get('/api/not_existing_car_plate/')
		self.assertEqual(request.status_code, 404)
		self.assertIs("name" not in request.json(), True)