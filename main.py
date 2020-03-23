from totalvoice.cliente import Cliente
from flask import Flask, escape, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

access_token = "24aa25e471711f0f8cb1a69dc7daf216"

cliente = Cliente(access_token, 'https://api2.totalvoice.com.br')


##########################################
############# csgleirbagti@ ##############
##########################################


@app.route('/')
def index():
    return render_template('index.html', alerta = None)


# #Cria sms
@app.route('/sms/enviar_sms/', methods=['POST'])
def enviar_sms():
    numero_destino = request.form['numero_destino']
    mensagem = request.form['sms_txt']
    print(f"Número -> {numero_destino} \n\nMensagem -> {mensagem}")
    response = cliente.sms.enviar(numero_destino, mensagem)
    # print(response)
    return render_template('index.html', alerta = f"Teste SMS - mensagem enviada para o número: {numero_destino}")


# TTS
# Módulo responsável por criação de Audios.
@app.route('/tts/enviar/', methods=['POST'])
def enviar_mensagem_deaudio():
    numero_destino = request.form['numero_destino']
    mensagem = request.form['tts_txt']
    response = cliente.tts.enviar(numero_destino, mensagem)
    print(response)
    return render_template('index.html', alerta = f"Teste TTS - mensagem enviada para o número: {numero_destino}")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='4811')
    
