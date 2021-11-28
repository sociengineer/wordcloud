# from django.http import JsonResponse
   
from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
import pandas as pd
   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartjs/index.html')
   


data = []
df = pd.read_csv('chartjs/data/hotel_review.csv')
for index, review in df.iterrows():
    temp_dict = {}
    temp_dict['text'] = review['text']
    temp_dict['size'] = review['frequency']
    data.append(temp_dict)
   
class ChartData(APIView):   
    def get(self, request, format = None):
        return Response(data)