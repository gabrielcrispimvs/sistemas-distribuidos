## Como Rodar o Projeto

1. Instale as dependências:
````
pip install -r requirements.txt
````

2. Execute o servidor Flask:
````
python3 app.py
````

3. Inicie o Servidor SMTP Local
````
python3 -m smtpd -c DebuggingServer -n localhost:1025
````

4. Acesse a aplicação **http://127.0.0.1:5000**

