from flask import Flask, jsonify, request
from flask_restx import Resource, Api
from flask_mail import Mail, Message
from dotenv import load_dotenv
from schema.emailSchema import EmailSchema
import os

load_dotenv()

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ["MAIL_USERNAME"]
app.config['MAIL_PASSWORD'] = os.environ["MAIL_PASSWORD"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
api = Api(app)


@api.route("/email")
class Email(Resource):
    def get(self):
        return jsonify({'hello': 'world'})

    def post(self, ):
        data = request.get_json()

        emailSchema = EmailSchema(request=data)
        validate = emailSchema.validator()
        if len(validate) > 0:
            error = {
                "status": "error",
                "message": validate
            }
            return error, 400

        nome, email, assunto, mensagem = emailSchema.descontruct()

        # msg = Message(assunto,
        #               sender='andreluizpsn97@hotmail.com', recipients=[email])
        # msg.body = mensagem
        # mail.send(msg)

        return jsonify({"Enviado para: ": email})


if __name__ == "__main__":
    app.run(debug=True)
