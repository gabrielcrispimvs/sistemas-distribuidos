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

<br>

## Próximas etapas

#### Estrutura do Projeto
Aqui está como o projeto pode evoluir em termos de estrutura:
````
projeto-final/
│
├── app.py                   # Servidor Flask, centraliza as rotas e funções principais
├── email_service.py         # Código para envio de e-mails, incluindo algoritmos de failover
├── middleware.py            # Lógica do middleware para gestão de filas e balanceamento
├── requirements.txt         # Lista de dependências do projeto
│
├── templates/               # Arquivos HTML
│   └── index.html           # Página principal com o formulário de envio
│
└── static/                  # Arquivos CSS e JS
    └── style.css            # CSS opcional
````

### Passo-a-Passo das Próximas Partes
1. Separação da Lógica de Envio de E-mails
- Objetivo: Mover a lógica de envio de e-mails para um arquivo dedicado (email_service.py), facilitando a manutenção e organização do código.
- Código: Refatore enviar_email para que possa ser chamado de qualquer parte do projeto.
2. Desenvolver o Middleware para Gestão de Filas
- Crie middleware.py para gerenciar a lógica de filas e dividir a lista de e-mails em lotes.
- Passos:
    - Configuração da Fila de Mensagens: Utilize um serviço como Redis ou RabbitMQ. Cada lote de e-mails será uma mensagem na fila.
    - Funções de Balanceamento de Carga: Implemente uma função para distribuir os lotes entre os servidores de e-mail. Inicialmente, você pode usar um balanceador simples, como Round-robin.
3. Implementar Algoritmos de Failover (Retry e Circuit Breaker)
- Retry: No email_service.py, implemente uma lógica de retry para reenviar o e-mail em caso de falha.
    - Exemplo: Use uma estratégia de tempo crescente (exponencial) entre tentativas. Após um certo número de tentativas, registre o e-mail como “não enviado”.
- Circuit Breaker: Monitore os servidores de e-mail para “desativar” servidores com falhas recorrentes, evitando sobrecarga.
    - Estrutura: Configure um contador de falhas para cada servidor. Se ele ultrapassar um limite, o servidor é pausado por um tempo.
4. Implementar o Monitoramento com Heartbeats
- Objetivo: Monitore os servidores de e-mail periodicamente para garantir que estejam ativos.
- Função Heartbeat: No middleware.py, crie uma função que envia “pings” periódicos aos servidores de e-mail.
- Lógica de Redistribuição: Se um servidor não responder ao ping, remova-o temporariamente da lista de servidores ativos.

### Resumo das Funções por Arquivo
- ``app.py``: Centraliza as rotas e chama funções do middleware.
- ``middleware.py``: Gerencia a fila de e-mails, divide os e-mails em lotes e distribui entre os servidores.
- ``email_service.py``: Lida com o envio real dos e-mails e os algoritmos de failover.

