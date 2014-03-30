from flask import Flask, url_for, render_template, jsonify, request
from pymongo import MongoClient
from filter import *
from sendgrid import SendGridClient, Mail
import cloud_elements
import json
from settings import *
import video_merger

app = Flask(__name__)
app.debug = True


@app.route('/', methods = ['GET'])
def hello():
		return render_template('index.html')


@app.route('/trans', methods = ['POST','GET'])
def translate(): 
	body = request.form['body']
	clean = getWords(getSentences(body))
	text = []
	for k, v in clean.items():
		for word in v:
			text.append("./videos/"+ word + ".mp4")
	video_name = video_merger.makeVideo(text)

	return render_template("test.html", body=video_name )

@app.route('/sendmail', methods = ['POST'])
def sendmail():
	# get form fields
	send_to = request.form['to']
	subject = request.form['subject']
	filename = request.form['filename']

	# upload video to dropbox
	client = cloud_elements.ElementsConnector()
	upload = {
	  'path': "/text2hand",
	  'description': subject,
	  'tag': "text2hand"
	}
	# file path in dropbox
	dropbox_file = "videos/%s" % filename
	files = [dropbox_file]
	# upload file on dropbox
	res = client.invoke(httpMethod='post', providerName='document', elementToken = "3faa91bf8cf909dbf2f4123af86d51f0", apiMethodName='uploadFiles', payload=upload, files=files)
	search = {
    'path': res['records'][0]['path']
	}
	# get url of uploaded file
	res = client.invoke(httpMethod='get', providerName='document', elementToken = "3faa91bf8cf909dbf2f4123af86d51f0", apiMethodName='getDownloadLink', params=search)
	url = res['value']
	# send mail
	sg = SendGridClient(sg_user, sg_pass)
	message = Mail()
	message.set_from('text2hand@hackpr.com')
	message.add_to(send_to)
	message.set_subject(subject)
	message.set_html("<p><strong>Here is your video</strong><br>Video Link: <a href='%s'>Dropbox</a></p>" % url)
	try:
		status, msg = sg.send(message)
	except Exception, e:
		raise e
		
	return render_template('sendmail.html', send_to = send_to, subject = subject, filename = filename, res = res)

if __name__ == '__main__':
	app.run()