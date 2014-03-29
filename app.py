from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app.debug = True

@app.route('/', methods = ['GET'])
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run()