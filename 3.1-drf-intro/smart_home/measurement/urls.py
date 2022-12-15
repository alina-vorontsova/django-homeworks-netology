from django.urls import path

from .views import SensorListView, SensorDetailView, MeasurementCreationView


urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensors'),
    path('sensors/<pk>/', SensorDetailView.as_view(), name='sensor'),
    path('measurements/', MeasurementCreationView.as_view(), name='measurement'),
]
