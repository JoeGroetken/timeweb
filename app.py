from flask import Flask, render_template, request
import os
import subprocess 
import re

app = Flask(__name__)
app.secret_key = 'bvu9bvtu9[ojervnu024v0ujtbu9ruv905t4b9i5ghu0tg'

rawDate = subprocess.run(['date', "+%b %d, %Y, %H:%M"], stdout=subprocess.PIPE, universal_newlines=True)
date = rawDate.stdout

def formatDate(time):
	
    time = re.sub('\n', '', date)
    return time

appDate = formatDate(date)

@app.route('/')
def index():
	return appDate
