from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/exchange_rate', methods=['GET'])
def get_exchange_rate():
    base_currency = request.args.get('base', 'USD')
    target_currency = request.args.get('target', 'BRL')

    # Substitua pelo endpoint correto da API do Banco Central
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos?formato=json'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        data = response.json()
        
        # Processar e retornar os dados necessários
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)