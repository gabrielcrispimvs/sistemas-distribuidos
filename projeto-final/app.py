from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Lista para armazenar e-mails enviados
emails_enviados = []

from datetime import datetime

# Função para enviar e-mail
def enviar_email(destinatario, corpo, titulo):
    servidor_smtp = 'localhost'
    porta = 1025
    usuario = 'test@localhost'
    
    servidor = smtplib.SMTP(servidor_smtp, porta)
    servidor.set_debuglevel(1)  # Nível de debug para o servidor

    mensagem = MIMEMultipart()
    mensagem['From'] = usuario
    mensagem['To'] = destinatario
    mensagem['Subject'] = titulo  # Usando o título do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    servidor.sendmail(usuario, destinatario, mensagem.as_string())
    servidor.quit()

    # Armazena o e-mail enviado na lista com a data e hora do envio
    data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emails_enviados.append((usuario, destinatario, corpo, data_envio, titulo))

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o envio
@app.route('/enviar', methods=['POST'])
def enviar():
    lista_emails = request.form['lista_emails'].splitlines()
    corpo_email = request.form['corpo_email']
    titulo_email = request.form['titulo_email']

    for destinatario in lista_emails:
        enviar_email(destinatario.strip(), corpo_email, titulo_email)

    # Renderiza um template de confirmação com o link para a lista de e-mails
    return render_template('confirmacao.html')

# Rota para listar e-mails enviados
@app.route('/emails')
def lista_emails():
    return render_template('lista_emails.html', emails=emails_enviados)

if __name__ == '__main__':
    app.run(debug=True)