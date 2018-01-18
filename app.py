"""
API para utilidades del sitio web cesarmorales.website
"""

from flask import Flask, request
from flask_cors import CORS
from sendEmail import send_email
from errorSendEmail import SendError

app = Flask(__name__)
CORS(app)


@app.route('/send_email', methods=['POST'])
def post_send_email():
    response = ''
    if request.method == 'POST':
        try:
            name = request.form['name']
            from_addr = request.form['email']
            subject = request.form['subject']
            msg_text = request.form['message']

            send_email(name, from_addr, subject, msg_text)
            response = 'OK'
        except SendError as inst:
            response = inst.message
        except Exception:
            response = 'Error desconocido.'

    return response


if __name__ == '__main__':
    app.run(debug=True)
