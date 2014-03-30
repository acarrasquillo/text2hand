from flask import Flask, url_for, render_template, jsonify, request
from pymongo import MongoClient
from flaskext.coffee2js import coffee2js

app = Flask(__name__)
app.debug = True

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