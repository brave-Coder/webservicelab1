from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Temperature
from .serializer import TemperatureSerializer
from django.http import JsonResponse

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

def get_latest_readings(request):
    latest_reading = Temperature.objects.latest('timestamp')
    data = {
        'temperature': latest_reading.temperature,
        'humidity': latest_reading.humidity
    }
    return JsonResponse(data)

relay_state = False  # Initially, relay is OFF

@csrf_exempt
def relay_control_view(request):
    global relay_state

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            relay_state_input = data.get('relay_state', None)

            if relay_state_input is not None:
                # Update relay state based on input
                if relay_state_input == "true":
                    relay_state = True
                    # Add code here to physically turn the relay ON
                    return JsonResponse({'message': 'Relay turned ON', 'relay_state': 'true'}, status=200)
                elif relay_state_input == "false":
                    relay_state = False
                    # Add code here to physically turn the relay OFF
                    return JsonResponse({'message': 'Relay turned OFF', 'relay_state': 'false'}, status=200)
                else:
                    return JsonResponse({'error': 'Invalid relay state'}, status=400)
            else:
                return JsonResponse({'error': 'No relay state provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    elif request.method == 'GET':
        # Return the current relay state
        return JsonResponse({'relay_state': 'true' if relay_state else 'false'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_relay_status(request):
    """
    This view returns the current relay status in JSON format.
    It responds with either "true" or "false" depending on the state.
    """
    global relay_state

    # Return relay status as JSON
    return JsonResponse({'relay_state': relay_state})