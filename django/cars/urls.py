from django.urls import path
from cars.views import IndexView, CarDetailView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('detail/', CarDetailView.as_view(), name="detail"),
]