from django.urls import path
from .views import TemperatureDetailView,  TemperatureListView, TemperatureCreateAPIView
from . import views
urlpatterns = [
    path('temperatures/', TemperatureListView.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureDetailView.as_view(), name='temperature-detail'),
    path('temperature/', TemperatureCreateAPIView.as_view(), name='temperature-create'),
    path('dashboard/', views.dashboard, name="dashboard")

]
