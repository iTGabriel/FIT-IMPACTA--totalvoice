from totalvoice.cliente import Cliente
from flask import Flask, escape, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

access_token = "SEU TOKEN"

cliente = Cliente(access_token, 'https://api2.totalvoice.com.br')


##########################################
############# csgleirbagti@ ##############
##########################################


@app.route('/')
def index():
    return render_template('index.html', alerta = None)


# TTS
# Módulo responsável por criação de Audios.
@app.route('/tts/enviar/', methods=['POST'])
def enviar_mensagem_deaudio():
    numero_destino = request.form['numero_destino']
    mensagem = request.form['tts_txt']
    response = cliente.tts.enviar(numero_destino, mensagem)
    print(response)
    return render_template('index.html', alerta = f"Teste TTS - mensagem enviada para o número: {numero_destino}")


#Cria chamada
# @app.route('/ligacao/chamar/<numero_origem>/<numero_destino>')
# def realizar_chamada(numero_origem, numero_destino):
#     response = cliente.chamada.enviar(numero_origem, numero_destino)
#     print(response)
#     return "Teste de 'ligação' executado"


# #Cria sms
# @app.route('/sms/enviar_msmsimples/<numero_destino>/<mensagem>')
# def enviar_sms(numero_destino, mensagem):
#     response = cliente.sms.enviar(numero_destino, mensagem)
#     print(response)
#     return "Teste de 'SMS enviado' executado"



# @app.route('/validacao/numero/<numero_avalidar>')
# #cria um registro validaNumero que irá checar se o número é válido
# def verifica_numero(numero_avalidar):
#     response = cliente.valida_numero.criar(numero_avalidar)
#     print(response)
#     return "Teste de 'validação de número' executado"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='4811')
    
