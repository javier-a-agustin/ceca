from cars.models import Car
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'index.html'

class CarDetailView(View):

    def post(self, request):
        """
            Given a car_plate from the request.POST object, return a html response with a message
        """
        car_plate = request.POST.get('car_plate')
        try:
            car = Car.objects.get(plate=car_plate)
            car_name_mesage = f"The name for the car plate {car_plate} is {car.name}"
            messages.success(request, car_name_mesage)
        except Exception as e:
            print(e)
            messages.warning(request, "Could not find a car with the requested plate")
        return render(request, 'response.html')
        

   