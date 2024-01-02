from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__)
app.secret_key = 'amendoim678'

# Dados para app acessar o email receptor
email = 'contato.kaio.abreu@gmail.com'
senha = 'urqy hwrn pugu sqvw'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('portfólio.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/inicio_dest')
def voltar_site():
    return render_template('inicio_dest.html')

@app.route('/primeirapagina')
def primeira_pagina():
    return render_template('primeirapagina.html')

@app.route('/inicio_dest')
def segunda_pagina():
    return render_template('inicio_dest.html')

@app.route('/lago_peyto')
def terceira_pagina():
    return render_template('lago_peyto.html')

@app.route('/ilha_meeru')
def quarta_pagina():
    return render_template('ilha_meeru.html')

@app.route('/rio_sub_puerto_princesa')
def quinta_pagina():
    return render_template('rio_sub_puerto_princesa.html')

@app.route('/aurora_boreal')
def sexta_pagina():
    return render_template('aurora_boreal.html')

@app.route('/cataratas_iguacu')
def septa_pagina():
    return render_template('cataratas_iguacu.html')

@app.route('/inicio_dest')
def voltar_pagina():
    return render_template('inicio_dest.html')

@app.route('/destinos')
def tabela_destinos():
    return render_template('destinos.html')

@app.route('/galeria_viagens')
def galeria_viagens():
    return render_template('galeria_viagens.html')

@app.route('/destino1')
def destino1():
    return render_template('destino1.html')

@app.route('/destino2')
def destino2():
    return render_template('destino2.html')

@app.route('/destino3')
def destino3():
    return render_template('destino3.html')

@app.route('/destino4')
def destino4():
    return render_template('destino4.html')

@app.route('/destino5')
def destino5():
    return render_template('destino5.html')

@app.route('/destino6')
def destino6():
    return render_template('destino6.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"], 
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender = app.config.get("MAIL_USERNAME"),
            recipients= ['kaio.abreu@fatec.sp.gov.br', app.config.get("MAIL_USERNAME")],
            body = f'''

            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte 
            mensagem:

            {formContato.mensagem}

            '''
        )
    try:
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    except Exception as e:
        print(f"Erro no envio de e-mail: {e}")
        flash('Erro ao enviar a mensagem. Verifique as configurações de e-mail.')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)