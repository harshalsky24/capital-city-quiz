import random
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

API_URL = "https://countriesnow.space/api/v0.1/countries/capital"

class GetCountry(APIView):
    def get(self, request):
        res = requests.get(API_URL).json()
        # Filter out countries with missing capital
        data = [item for item in res['data'] if item.get('capital')]
        country_data = random.choice(data)
        return Response({
            "country": country_data['name'],
            "correct_capital": country_data['capital']
        })

class CheckCapital(APIView):
    def post(self, request):
        answer = request.data.get('answer', '').strip().lower()
        actual = request.data.get('actual', '').strip().lower()  # must match key sent from Vue

        print(f"DEBUG: user_answer='{answer}', correct_capital='{actual}'")  # Optional debug

        if answer == actual:
            return Response({'result': 'correct'})
        return Response({'result': 'incorrect', 'correct_capital': actual})
