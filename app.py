from flask import Flask, render_template, request
import os
import subprocess 
import re

app = Flask(__name__)
app.secret_key = 'bvu9bvtu9[ojervnu024v0ujtbu9ruv905t4b9i5ghu0tg'

def formatDate():
    rawDate = subprocess.run(['date'], stdout=subprocess.PIPE, universal_newlines=True)
    date = rawDate.stdout

    dateArray = date.split(" ")
    dateArray.pop(0)
    dateArray.pop(3)
    newlineRemoval = dateArray[3]
    dateArray[3] = re.sub('\n', '', newlineRemoval)
    hmsToHm = dateArray[2].split(":")
    dateArray[2] = hmsToHm[0] + ":" + hmsToHm[1]

    returndate = dateArray[0] + " " + dateArray[1] + ", " + dateArray[3] + ", " + dateArray[2]
    return returndate

appDate = formatDate()

@app.route('/')
def index():
	return appDate
