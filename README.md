# t10
t10 challenge

Api desenvolvida pra o processo seletivo do t10. Para utilizá-la, será necessário ter instalado o docker e o python.

## Para utilizar a Api, siga os passos abaixo:

### 1. Crie um ambiente virtual python com o comando:
```python3 -m venv t10challenge```

### 2. Mude para a pasta do ambiente virtual criado e ative-o com:
```source bin/activate```
ou
```Scripts\activate```
para sistemas Windows

### 3. Baixe os arquivos do git dentro do ambiente virtual com:
```git clone https://github.com/MarcosVAdS/t10.git```

### 4. Instale as dependencias com:
```pip install -r requiremensts.txt```

### 5. Crie uma instancia do docker do banco rodando:
```docker build -t eg_postgresql .```

### 6. Rode o banco com: 
```docker run --rm -P --name pg_test eg_postgresql```

### 7. Faça as migrations do banco com:
```python manage.py migrate```

### 8. Crie um novo usuário do django com:
```python manage.py createsuperuser```

### 9. Inicie o Servidor django:
```python manage.py runserver```

## Para navegar

Aqui tem algumas rotas para utilizar a API.

- Acessa a administração da API (`http://localhost:8000/admin`).

- Utilizando o Swagger (`http://localhost:8000/`). Assim, pode-se ver todas as rotas e entender o que cada método faz.

- Visitar a aba de Empresas parceiras acesse. (`http://localhost:8000/partners/`).

- Visitar a aba de Requisição de débitos acesse. (`http://localhost:8000/debits/`).

- Visitar a aba de Usuários acesse. (`http://localhost:8000/users/`).

### Para fazer login, é utilizar o usuário criado no passo 6
