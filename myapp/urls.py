from django.urls import path
from .views import TemperatureDetailView,  TemperatureListView, TemperatureCreateAPIView, get_latest_readings, relay_control_view, get_relay_status
from . import views
urlpatterns = [
    path('temperatures/', TemperatureListView.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureDetailView.as_view(), name='temperature-detail'),
    path('temperature/', TemperatureCreateAPIView.as_view(), name='temperature-create'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('api/get-readings/', get_latest_readings, name='get_readings'),
    path('relay-control/', relay_control_view, name='relay_control'),
    path('getrelaystatus/', get_relay_status, name='get_relay_status'),
]

