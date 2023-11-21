import os
from flask import Flask, request
from external.api.enviarEmail import email_bp
from external.api.cobranca import cobranca_bp
from external.api.cartao import cartao_bp
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# csrf = CSRFProtect(app)

# app.config['SECRET_KEY'] = os.urandom(64).hex()

app.register_blueprint(email_bp)
app.register_blueprint(cobranca_bp)
app.register_blueprint(cartao_bp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))