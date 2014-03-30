import os
from os import listdir
from os.path import dirname
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client['text2hand']
video_match = db['video_match']

path = os.path.abspath(os.path.dirname(__file__))
video_list_path = path + '/../videos'

for f in listdir(video_list_path):
	entry_word = f.replace(".mp4", "")
	entry_video_url = f
	entry = {"word": entry_word, "video_url": '/videos/'+entry_video_url}
	video_match.insert(entry)

video_match.ensure_index('word',1)