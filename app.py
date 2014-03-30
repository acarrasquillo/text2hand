from flask import Flask, url_for, render_template, jsonify, request
from pymongo import MongoClient
from filter import *
from sendgrid import SendGridClient, Mail
# from settings import *

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET','POST'])
def hello():
	if (request.method == 'POST'):
		to = request.form['to']
		subject = request.form['subject']
		return render_template('index.html', to = to, subject = subject)
	else :
		return render_template('index.html')

@app.route('/trans', methods = ['POST','GET'])
def translate(): 
	body = request.form['body']
	clean = getWords(getSentences(body))
	text = ""
	for k, v in clean.items():
		for word in v:
			text = text + "|" + word + ".mp4"




	return render_template("test.html", body=text )

if __name__ == '__main__':
	app.run()