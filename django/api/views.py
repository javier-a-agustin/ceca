from api.models import Car
from rest_framework import generics
from api.serializers import CarSerializer

class RetrieveCarView(generics.RetrieveAPIView):
    """
        Retrieve view.
        From a given car_plate returns the car name or 404.
        Uses CarSerializer and search the row by plate.

        url example: 
            http://localhost:8000/api/CAR_PLATE/
            where CAR_PLATE is the string to search for
        response example:
            status_code: 200
                {
                    "name": "CAR_NAME"
                }
            status_code: 404
                {
                    "detail": "Not found."
                }
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'plate'