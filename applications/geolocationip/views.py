import requests
import json

from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes 
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.urls import reverse
#from django.shortcuts import render
#from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from Geolocation.settings.base import get_secret

## With Django rest framework Requests and Responses
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer,JSONRenderer]) 
def get_ip_tracker(request):
    ip_address = request.GET.get('IP','')
    fields = "status,query,country,timezone,lat,lon,isp"
    api_url = requests.get(f'http://ip-api.com/json/{ip_address}?fields={fields}') 
    api_key = get_secret('API_KEY')
    data = json.loads(api_url.content)
    data['api_key'] = api_key
    status = data.get('status')
    
    if status == "fail":
        messages.error(request,'You have entered an invalid IP address!')
        return HttpResponseRedirect(reverse('ip_app:ip_tracker'))
    return Response(data,template_name='geolocationip/home.html')

## With Django class-based views
# class GetIpTracker(View):
#     def get(self,request,*args,**kwargs):
#         ip_address = request.GET.get('IP','')
#         fields = "status,query,country,timezone,lat,lon,isp"
#         api_url = requests.get(f'http://ip-api.com/json/{ip_address}?fields={fields}') 
#         api_key = get_secret('API_KEY')
#         geodata = json.loads(api_url.content)
#         geodata['api_key'] = api_key
#         status= geodata.get('status')
#         if status == "fail":
#             messages.error(request,'You have entered an invalid IP address!')
#             return HttpResponseRedirect(reverse('ip_app:home'))
#         return render(request,'geolocationip/home.html',geodata)
