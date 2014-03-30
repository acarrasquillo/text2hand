import os
from os import listdir
from os.path import dirname
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client['text2hand']
video_match = db['video_match']


path = os.path.abspath(os.path.dirname(__file__))
videos_import_path = path + '/../videos'

video_path = dirname(path) + '/videos/'
print video_path

for f in listdir(videos_import_path):
	entry_word = f.replace(".mp4", "")
	entry_video_url = video_path + f
	entry = {"word": entry_word, "video_url": entry_video_url}
	video_match.insert(entry)