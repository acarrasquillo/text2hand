from flask import Flask, url_for, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET'])
def hello():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()