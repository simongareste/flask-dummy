from flask import Flask
from passlib.hash import sha512_crypt; 

app = Flask(__name__)

@app.route("/")
def hello():
    return "You are probably looking for /<password_you_want_to_encode> endpoint"

@app.route("/<password>")
def encrypt_password(password):
    encrypted_password = sha512_crypt.encrypt(password)
    return "%s => %s" % (password, encrypted_password)
