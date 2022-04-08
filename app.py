from smtplib import SMTPException

from flask import Flask, jsonify, Response
from utils import create_random_numbers
from typing import List

from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='email-smtp.us-east-1.amazonaws.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'seuusuario'
app.config['MAIL_PASSWORD'] = 'suasenha'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


def send_email(title: str, message: any, recipients: List[str]):

    try:

        msg = Message(title, sender='email@cemail.com.br', recipients=recipients)
        msg.body = str(message)
        mail.send(msg)

    except Exception:
        raise SMTPException("Erro no serviço de envio de email")


@app.route('/send_email')
def send_email_method():
    try:
        number = create_random_numbers(19)

        send_email('Numero Aleatório', number, ['tratativasdeexecoes@email.com'])

        return jsonify(message="email enviado com sucesso"), 200

    except SMTPException as error:

        return jsonify(message=str(error)), 503

    except TypeError as error:

        return jsonify(message=str(error)), 500

    except Exception as e:

        return jsonify(message="Aconteceu um erro inesperado no serviço"), 500


if __name__ == '__main__':
    app.run()
