#! /usr/bin/env python
#from app import app

#app.run(debug=True, host="0.0.0.0", port=3128)

import json
#from apiclient.discovery import build_from_document, build
#import httplib2
import random

#from oauth2client.client import OAuth2WebServerFlow

from flask import Flask, render_template, session, request, redirect, url_for, abort

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

app = Flask(__name__)


@app.route('/')
def login():
  os.system("python3 Checksum.py")

if __name__ == '__main__':
  app.secret_key = 'hello world'
  app.run(host='0.0.0.0')