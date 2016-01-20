from flask import Flask
from passlib.hash import sha512_crypt; 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/password/<password>")
def encrypt_password(password):
    encrypted_password = sha512_crypt.encrypt(password)
    return "%s => %s" % (password, encrypted_password)
