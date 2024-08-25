Projeto Django - Cadastro de Usuário e API de Câmbio
Visão Geral

Este projeto é uma aplicação web desenvolvida em Django para consultar e visualizar a cotação do dólar utilizando a API do Banco Central do Brasil. A aplicação oferece funcionalidades básicas de autenticação de usuários e exibe a taxa de câmbio em gráficos interativos. O projeto inclui gráficos para visualizar as taxas de câmbio e funcionalidades básicas de CRUD.

Funcionalidades

Autenticação de Usuários Registro de Usuário: Permite que novos usuários se registrem criando uma nova conta. Login de Usuário: Usuários registrados podem fazer login para acessar funcionalidades protegidas. Logout de Usuário: Usuários autenticados podem sair da conta.
Visualização da Taxa de Câmbio Consulta da API: Consulta a API do Banco Central para obter a taxa de câmbio do dólar. Gráficos Interativos: Exibe a taxa de câmbio em gráficos usando Chart.js para facilitar a visualização das variações.
projeto_django/ │ ├── myapi/ │ ├── migrations/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── tests.py │ ├── urls.py │ ├── views.py │ └── templates/ │ ├── home.html │ ├── registration/ │ │ ├── login.html │ │ └── register.html │ └── exchange_rate.html │ ├── projeto_cad_usuario/ │ ├── init.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ ├── wsgi.py │ ├── manage.py └── venv/

Estrutura do Projeto

Pastas e Arquivos projeto_django/: Diretório raiz do projeto. myapi/: Aplicação Django que contém a lógica para a taxa de câmbio e autenticação. migrations/: Arquivos de migração do banco de dados. models.py: Define o modelo ApiClick para registrar interações com a API. views.py: Implementa as views para exibir a taxa de câmbio e páginas de autenticação. urls.py: Define as URLs da aplicação myapi. templates/: Contém templates HTML para renderizar as páginas. home.html: Página inicial com informações sobre a aplicação. registration/: Templates para autenticação. login.html: Formulário de login. register.html: Formulário de registro. exchange_rate.html: Página para visualizar a taxa de câmbio em gráficos. projeto_cad_usuario/: Configurações principais do projeto Django. settings.py: Configurações do projeto, incluindo o banco de dados. urls.py: Configuração das URLs principais do projeto. wsgi.py: Configuração para o servidor WSGI. manage.py: Script de administração para comandos Django. venv/: Ambiente virtual com as dependências do projeto.
Funcionalidades em Detalhe
Autenticação de Usuários
Registro:
URL: /register/ Página para criar uma nova conta de usuário. Após o registro, o usuário é redirecionado para a página de login. Login:

URL: /login/ Página para autenticação de usuários registrados. Após o login, o usuário é redirecionado para a página inicial. Logout:

URL: /logout/ Permite que o usuário encerre a sessão. Visualização da Taxa de Câmbio Consulta da API:

URL: /api/exchange_rate/ Endpoint que consulta a API do Banco Central e retorna a taxa de câmbio do dólar em formato JSON. Visualização com Gráficos:

URL: /exchange_rate/ Página que exibe a taxa de câmbio em gráficos interativos usando Chart.js. O gráfico mostra a flutuação da taxa de câmbio ao longo do tempo. Configuração e Execução Instalação:

Clone o repositório e crie um ambiente virtual: bash Copiar código python -m venv venv source venv/bin/activate # No Windows: venv\Scripts\activate Instale as dependências: bash Copiar código pip install -r requirements.txt Configuração do Banco de Dados:

Configure as credenciais do banco de dados no arquivo settings.py. Migrações:

Aplique as migrações para criar as tabelas do banco de dados: bash Copiar código python manage.py makemigrations python manage.py migrate Execução:

Inicie o servidor de desenvolvimento: bash Copiar código python manage.py runserver

|O servidor estará disponível em http://127.0.0.1:8000/. |
