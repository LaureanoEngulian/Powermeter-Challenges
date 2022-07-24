from cmath import inf
from django.forms import Media
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from powermeter.models import Medicion

# Create your views here.
@api_view(['POST'])
def save_measures(request):
    data = request.data
    sensor_data = data.get('sensor_data')
    for i in sensor_data:
        print(i)
        measure = Medicion(sensor_data=float(i))
        measure.save()

    return Response({'sensor_data': sensor_data})

@api_view(['GET'])
def max_measure(request):
    measures = Medicion.objects.values_list()
    x = -inf
    for i in measures:
        if i[1] > x:
            x = i[1]
        else:
            pass
    return Response({'max': x})

@api_view(['GET'])
def min_measure(request):
    measures = Medicion.objects.values_list()
    x = inf
    for i in measures:
        if i[1] < x:
            x = i[1]
        else:
            pass
    return Response({'min': x})

@api_view(['GET'])
def avg_measure(request):
    measures = Medicion.objects.values_list()
    x = 0
    for i in measures:
        x += i[1]
    avg = x/len(measures)

    return Response({'avg': avg})


