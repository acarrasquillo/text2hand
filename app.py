from flask import Flask, url_for, render_template, jsonify, request
from pymongo import MongoClient
from sendgrid import SendGridClient, Mail
from flaskext.coffee2js import coffee2js
from settings import *

app = Flask(__name__)
app.debug = True

sg = SendGridClient(sg_user, sg_pass)

def sendmail(email,subject, html):
	try:
		message = Mail()
		message.set_from('text2hand@hackpr.com')
		message.add_to(email)
		message.set_subject(subject)
		message.set_html(html)
		status, msg = sg.send(message)
		return True
	except:
		return False

coffee2js(app, js_folder='js', coffee_folder='src/coffee')

@app.route('/', methods = ['GET','POST'])
def hello():
	if (request.method == 'POST'):
		to = request.form['to']
		subject = request.form['subject']
		return render_template('index.html', to = to, subject = subject)
	else :
		return render_template('index.html')


if __name__ == '__main__':
	app.run()