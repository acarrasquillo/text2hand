from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app.debug = True

@app.route('/', methods = ['GET'])
def hello():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()