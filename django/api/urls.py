from django.urls import path
from api.views import RetrieveCarView

urlpatterns = [
	path('<plate>/', RetrieveCarView.as_view(), name="retrieve_car_by_name"),
]