# flask-IT
A flask app to get the password for Ansible

## Features

* Echoes <somepassword> and a sha512 encryption of <somepassword> when 
  /somepassword is called. This is the main and only goal of this app.
  And yes it could be easier to do this, but I wanted to try flask.

## Requirements

* python 2.7
* pip
* flask module
* passlib module

## Install

* Clone the repository
* Install prerequisites, possibly with `pip install -r requirements.txt`
* Execute the wsgi.py file

## Configuration

* Server is by default launched at 127.0.0.1:5000


