from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import requests

@login_required
def home(request):
    return render(request, 'home.html')

def exchange_rate(request):
    base_currency = request.GET.get('base', 'USD')
    target_currency = request.GET.get('target', 'BRL')
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos?formato=json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)