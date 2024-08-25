from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
import requests
from django.http import JsonResponse
from .models import ApiClick

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Fazer login automático após o registro
            return redirect('home')  # Redirecionar para a página inicial
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirecionar para a página inicial após o login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')  # Redirecionar para a página inicial após o logout
    return render(request, 'registration/logged_out.html')

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

        # Registra o clique
        ApiClick.objects.create(ip_address=request.META.get('REMOTE_ADDR'))

        # Renderiza o template com os dados
        return render(request, 'api_data.html', {'data': data})
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def exchange_rate_view(request):
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos?formato=json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        data = response.json()
        # Formatar os dados conforme necessário
        formatted_data = [{'data': item['data'], 'valor': item['valor']} for item in data]
    except requests.RequestException as e:
        # Se houver um erro, pode retornar uma mensagem de erro ou um conjunto vazio de dados
        formatted_data = []
    
    return render(request, 'exchange_rate.html', {'exchange_rate_data': formatted_data})

