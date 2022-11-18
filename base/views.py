from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data )

@api_view()
def advocate_list(request):
    data = ['Dennis', 'Tadas']
    return JsonResponse(data, safe=False)

@api_view()
def advocate_detail(request, username):
    data = username
    return JsonResponse(data, safe=False)
